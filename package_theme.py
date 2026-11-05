"""Script to package RemNote themes into ready-to-upload ZIP files."""

from pathlib import Path
import zipfile


def build_theme_zip(theme_dir: Path, output_zip: Path) -> None:
    required_files = ["manifest.json", "theme.css", "README.md"]
    for filename in required_files:
        if not (theme_dir / filename).exists():
            raise FileNotFoundError(f"Missing required file: {theme_dir / filename}")

    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for filename in required_files:
            file_path = theme_dir / filename
            zf.write(file_path, arcname=filename)
            print(f"  Added {filename} to {output_zip.name}")


def main() -> None:
    workspace_dir = Path(__file__).parent.resolve()
    themes = [d for d in workspace_dir.iterdir() if d.is_dir() and (d / "manifest.json").exists()]

    if not themes:
        print("No themes found with manifest.json.")
        return

    for theme_dir in themes:
        zip_path = theme_dir / f"{theme_dir.name}-remnote-theme.zip"
        print(f"Packaging theme: {theme_dir.name} -> {zip_path.name}")
        build_theme_zip(theme_dir, zip_path)
        print(f"Done: {zip_path}\n")


if __name__ == "__main__":
    main()
