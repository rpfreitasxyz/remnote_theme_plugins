# Vantablack Focus Theme for RemNote

Um tema ultra-escuro (estilo OLED / Vantablack) para o RemNote projetado para máxima imersão, foco evidente e conforto visual.
Diferente de temas escuros genéricos, o Vantablack Focus combina superfícies em preto puro (`#000000`) com guias verticais de hierarquia luminosas (bullet threading) e âncoras/referências em cápsulas suaves que saltam aos olhos sem agredir a visão.

## Características Principais

O design do tema conta com os seguintes destaques:

- **Fundo Preto Puro (OLED / Vantablack):** Redução máxima de emissão de luz com editor em `#000000` e barras laterais em `#050505`.
- **Bullet Threading Evidente:** Linhas verticais de hierarquia nítidas e visíveis (`#2c2c2c`) que se iluminam em ciano elétrico (`#38bdf8`) ao passar o mouse ou interagir com os nós da árvore.
- **Foco Imersivo:** Ao editar ou focar em qualquer bloco de rem, uma demarcação lateral sutil com gradiente luminoso destaca instantaneamente o contexto de trabalho.
- **Links e Âncoras Suaves:** As referências de rem (`[[...]]`) e links são renderizados como cápsulas elegantes com borda translúcida e tom azul-gelo (`#7dd3fc`), legíveis e estéticas sem saturação excessiva.
- **Destaques Harmonizados:** Tons de marcação suaves que preservam o alto contraste sem gerar efeito ofuscante.

## Paleta de Cores

| Elemento | Hexadecimal | Propósito |
| :--- | :--- | :--- |
| Background Editor | `#000000` | Preto absoluto para máxima imersão e economia OLED |
| Background Sidebar | `#050505` | Barra lateral discreta e elegante |
| Background Elevated | `#0d0d0d` | Popups, omnibar e cartões de repetição |
| Linha de Threading (Inativo) | `#2c2c2c` | Guia vertical nítida conectando pais e filhos |
| Linha de Threading (Ativo) | `#38bdf8` | Guia iluminada com brilho em ciano luminoso |
| Acento e Foco | `#38bdf8` | Indicadores de foco, botões primários e seleções |
| Links e Âncoras | `#7dd3fc` | Referências e links suaves em tom azul-gelo |
| Fundo de Âncoras | `rgba(56, 189, 248, 0.08)` | Cápsula translúcida suave para referências |
| Texto Principal | `#dedede` | Branco atenuado para evitar cansaço visual |
| Texto em Destaque | `#ffffff` | Títulos e ênfases em negrito |

## Como Instalar no RemNote

Você pode utilizar o tema de duas formas:

### 1. Upload como Plugin de Tema

Os passos para instalação pelo pacote compactado:

1. Baixe o arquivo `vantablack-remnote-theme.zip` desta pasta.
2. No RemNote, acesse **Settings > Plugins and Themes**.
3. Clique na aba **Build**.
4. Clique em **Upload Theme** e escolha o arquivo `.zip`.
5. Confirme que o RemNote está com o modo escuro selecionado (**Settings > Theme > Dark**).

### 2. Pelo Powerup Custom CSS

Os passos para colar o código diretamente no RemNote:

1. No RemNote, pressione `Ctrl + P` (ou `Cmd + P`) e digite **Custom CSS**.
2. Clique no botão **Add Blank CSS Block**.
3. Copie todo o conteúdo do arquivo `theme.css` desta pasta e cole no bloco.
4. Dê o nome "Vantablack Focus" ao bloco e ative-o.

## Licença

Distribuído sob a licença MIT.
Consulte o arquivo `LICENSE` na raiz do repositório.
