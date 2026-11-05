# RemNote Theme Plugins

Coleção de temas e estilos personalizados para o RemNote desenvolvidos por [Rafael Freitas](https://github.com/rpfreitasxyz).
Este repositório contém temas organizados em pastas individuais prontos para instalação direta ou empacotamento como plugins.

## Temas Disponíveis

A lista de temas disponíveis atualmente no repositório:

- [Antigravity Dark Theme](./antigravity/): Tema escuro inspirado no visual moderno do Google Antigravity IDE, com tons de cinza espacial profundo (`#1f1f1f`), barras de ferramentas em `#181818`, acentos em azul elétrico (`#0078d4`), tipografia refinada e estilização completa para flashcards, omnibar, tabelas e referências.

## Estrutura do Repositório

A organização dos arquivos e pastas segue o seguinte padrão:

```text
remnote_themes/
├── LICENSE
├── README.md
├── package_theme.py
└── antigravity/
    ├── manifest.json
    ├── theme.css
    ├── snippet.css
    ├── README.md
    └── antigravity-remnote-theme.zip
```

## Como Gerar os Pacotes de Tema

O repositório inclui um utilitário em Python para empacotar qualquer pasta de tema em um arquivo `.zip` compatível com a aba Build do RemNote.

Para empacotar todos os temas presentes no workspace, execute o seguinte comando:

```bash
python package_theme.py
```

O script localizará todas as pastas que possuem `manifest.json` e gerará os arquivos `.zip` correspondentes prontos para upload.

## Pré-visualizador

A pasta [`visualizer`](./visualizer/) contém um servidor local que aplica o `theme.css` de qualquer tema sobre uma página do RemNote salva em `.mhtml`, com recarga automática ao salvar o CSS.

Os passos para usar:

1. Salve uma página do RemNote com o navegador (Ctrl+S, formato "Página da Web, único arquivo") como `visualizer.mhtml` na raiz do repositório.
2. Execute `python visualizer/serve.py` (use `--rebuild` para re-extrair um `.mhtml` novo).
3. Escolha o tema na barra no canto inferior direito, ou abra `http://127.0.0.1:8765/?theme=antigravity`.

O `.mhtml` e a página extraída contêm dados pessoais e ficam no `.gitignore`.

## Guia de Instalação no RemNote

Você pode aplicar qualquer tema deste repositório de duas formas:

### 1. Upload como Plugin de Tema

Os passos para enviar o arquivo compactado:

1. Acesse o RemNote e abra **Settings > Plugins and Themes**.
2. Clique na aba **Build**.
3. Clique em **Upload Theme** (ou **Upload Plugin**).
4. Selecione o arquivo `.zip` gerado dentro da pasta do tema desejado (ex: `antigravity/antigravity-remnote-theme.zip`).
5. Ative o tema na sua lista de plugins e confirme que o modo escuro do RemNote está selecionado.

### 2. Pelo Powerup Custom CSS (Código Direto)

Os passos para colar o código CSS diretamente nas suas notas:

1. No RemNote, pressione `Ctrl + P` (ou `Cmd + P` no Mac) e pesquise por **Custom CSS**.
2. Clique em **Add Blank CSS Block**.
3. Copie o conteúdo integral do arquivo `theme.css` da pasta do tema desejado e cole no bloco.
4. Nomeie o bloco com o nome do tema e ative o botão de alternância.

## Documentação Oficial

Para saber mais sobre as classes, seletores e diretrizes de desenvolvimento de temas para o RemNote, consulte a documentação oficial:

- [RemNote Plugin Docs - Custom CSS](https://plugins.remnote.com/custom-css)

## Licença

Este projeto é distribuído sob a licença MIT.
Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.

