"""Pré-visualizador local de temas do RemNote.

Uso:
    python visualizer/serve.py [--mhtml CAMINHO] [--port 8765] [--rebuild]

Na primeira execução, extrai o .mhtml salvo do RemNote para visualizer/page/
(sem scripts, sem os temas/CSS que o navegador tinha instalado) e sobe um servidor
que injeta o theme.css da pasta escolhida, com recarga automática ao salvar.
"""

import argparse
import email
import email.policy
import hashlib
import http.server
import json
import mimetypes
import re
import shutil
import threading
import webbrowser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent
PAGE = HERE / "page"
ASSETS = PAGE / "assets"

# Links de CSS que NÃO devem ir para o preview: temas de terceiros instalados no navegador
# do usuário (remnoteplugins.com) e CSS de extensões (arquivo na raiz do domínio, hash longo).
DROP_LINK = re.compile(
    r'<link[^>]*href="https://www\.remnoteplugins\.com/[^"]*"[^>]*>'
    r'|<link[^>]*href="https://www\.remnote\.com/[^/"]{40,}"[^>]*>'
)
DROP_LOC = re.compile(r"https://www\.remnoteplugins\.com/|https://www\.remnote\.com/[^/]{40,}$")
CSS_URL = re.compile(r"url\(\s*([\"']?)([^)\"']+)\1\s*\)")


def extract(mhtml: Path) -> None:
    """Converte o .mhtml em PAGE/index.html + PAGE/assets/*, com URLs reescritas para locais."""
    shutil.rmtree(PAGE, ignore_errors=True)
    ASSETS.mkdir(parents=True)
    msg = email.message_from_binary_file(mhtml.open("rb"), policy=email.policy.default)
    parts = [p for p in msg.walk() if not p.is_multipart() and p.get("Content-Location")]
    html_part = next(p for p in parts if p.get_content_type() == "text/html")
    names = {}
    for p in parts:
        loc = p["Content-Location"]
        if p is html_part or DROP_LOC.match(loc):
            continue
        ext = ".svg" if "svg" in p.get_content_type() else mimetypes.guess_extension(p.get_content_type()) or ""
        names[loc] = hashlib.sha1(loc.encode()).hexdigest()[:12] + ext

    def css_rewrite(text: str, base: str) -> str:
        def sub(m):
            ref = m.group(2)
            if ref.startswith("data:"):
                return m.group(0)
            absolute = urljoin(base, ref)
            return f'url("{names.get(absolute, absolute)}")'  # mesmo diretório que o CSS

        return CSS_URL.sub(sub, text)

    for p in parts:
        loc = p["Content-Location"]
        if loc not in names:
            continue
        data = p.get_payload(decode=True)
        if p.get_content_type() == "text/css":
            data = css_rewrite(data.decode("utf-8", "replace"), loc).encode()
        (ASSETS / names[loc]).write_bytes(data)

    html = DROP_LINK.sub("", html_part.get_payload(decode=True).decode("utf-8"))
    for loc in sorted(names, key=len, reverse=True):
        html = html.replace(loc, "assets/" + names[loc]).replace(loc.replace("&", "&amp;"), "assets/" + names[loc])
    (PAGE / "index.html").write_text(html, encoding="utf-8")
    print(f"Página extraída: {len(names)} recursos em {PAGE}")


def themes() -> dict:
    """Pastas irmãs de visualizer/ que tenham manifest.json + theme.css -> mtime do CSS."""
    return {
        d.name: (d / "theme.css").stat().st_mtime
        for d in sorted(ROOT.iterdir())
        if d.is_dir() and (d / "manifest.json").exists() and (d / "theme.css").exists()
    }


# Barra flutuante em Shadow DOM, para os temas em teste não a afetarem.
TOOLBAR = """<script>
(() => {
  const host = document.createElement('div');
  host.style.cssText = 'position:fixed;right:12px;bottom:12px;z-index:2147483647';
  const root = host.attachShadow({mode: 'open'});
  root.innerHTML = `<style>
    div{font:12px system-ui,sans-serif;background:#111;color:#eee;border:1px solid #444;border-radius:8px;
        padding:6px 10px;display:flex;gap:8px;align-items:center;box-shadow:0 4px 16px #0008}
    select,button{background:#222;color:#eee;border:1px solid #555;border-radius:4px;padding:2px 6px;font:inherit}
  </style><div>Tema <select></select><button>claro/escuro</button></div>`;
  const sel = root.querySelector('select');
  const link = document.createElement('link');
  link.rel = 'stylesheet';
  document.head.appendChild(link);
  let mt = {};
  const apply = () => {
    localStorage.setItem('theme', sel.value);
    link.href = sel.value ? `/__theme/${sel.value}.css?t=${mt[sel.value]}` : '';
  };
  const poll = async () => {
    const next = await (await fetch('/__themes', {cache: 'no-store'})).json();
    const changed = sel.value && next[sel.value] !== mt[sel.value];
    if (Object.keys(next).join() !== Object.keys(mt).join()) {
      const saved = sel.value || new URLSearchParams(location.search).get('theme') || localStorage.getItem('theme') || '';
      sel.innerHTML = '<option value="">Original (sem tema)</option>' +
        Object.keys(next).map(n => `<option>${n}</option>`).join('');
      sel.value = next[saved] ? saved : '';
    }
    mt = next;
    if (changed || !link.href) apply();
  };
  sel.onchange = apply;
  root.querySelector('button').onclick = () => {
    for (const el of [document.documentElement, document.body]) el.classList.toggle('dark');
  };
  document.body.appendChild(host);
  poll();
  setInterval(poll, 1000);
})();
</script>"""


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(PAGE), **kw)

    def _send(self, body: bytes, ctype: str):
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = unquote(urlparse(self.path).path)
        if path == "/__themes":
            return self._send(json.dumps(themes()).encode(), "application/json")
        if path.startswith("/__theme/") and path.endswith(".css"):
            name = path[len("/__theme/"):-4]
            if name in themes():  # whitelist evita path traversal
                return self._send((ROOT / name / "theme.css").read_bytes(), "text/css; charset=utf-8")
            return self.send_error(404)
        if path in ("/", "/index.html"):
            html = (PAGE / "index.html").read_text(encoding="utf-8")
            return self._send(html.replace("</body>", TOOLBAR + "</body>").encode(), "text/html; charset=utf-8")
        super().do_GET()

    def log_message(self, *args):
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mhtml", type=Path, default=ROOT / "visualizer.mhtml")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--rebuild", action="store_true", help="re-extrai o .mhtml")
    args = ap.parse_args()
    if args.rebuild or not (PAGE / "index.html").exists():
        extract(args.mhtml)
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    url = f"http://127.0.0.1:{args.port}/"
    print(f"Pré-visualizador em {url}  (Ctrl+C para sair)\nTemas: {', '.join(themes()) or 'nenhum'}")
    threading.Timer(0.5, webbrowser.open, args=[url]).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
