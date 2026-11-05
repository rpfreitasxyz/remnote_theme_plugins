# Alive-Dark Theme for RemNote

Um tema escuro que **responde a você**.
Mantém o conforto ergonômico do [ergo-dark](../ergo-dark/) (ardósia quente, texto em pergaminho, acento verde-eucalipto) e adiciona movimento com propósito: cada animação responde a uma ação sua e dura menos de 600ms.

## O que ganha vida

Os efeitos, todos feitos apenas com CSS:

- **Modo foco (profundidade de campo) e Palco Zen:** enquanto você digita em um bloco, os blocos distantes e a periferia da interface (sidebar, barra de topo e carrossel de datas) recuam suavemente para `opacity: 0.35`. Passar o mouse sobre as barras ou sobre qualquer bloco recuado os traz instantaneamente a `1.0`. A saída de foco é suave (700ms) e a entrada é rápida (140ms), para que o olho nunca seja puxado bruscamente.
- **Preservação de linhagem (Tarefa-Pai e Filhas):** a iluminação de foco concentra-se estritamente na tarefa ativa e na sua linhagem direta (o pai imediato e suas filhas conectadas pelo fio iluminado), sem vazar iluminação para blocos de outros ramos.
- **Bloco ativo:** holofote em gradiente que deriva lentamente, barra de margem em teal e um brilho que "respira" a cada 5,5s. Usa `box-shadow`, então o texto nunca se desloca ao focar.
- **Despertar semântico na linha ativa:** palavras em **negrito** ganham um leve *bloom* dourado quente (`text-shadow`), termos em *itálico* acendem em sage botânico, referências e links acendem em azul elétrico luminoso (`#38bdf8`) e blocos de `código` acendem a borda. A formatação ganha vida sob a sua digitação.
- **Micro-recompensa de linha nova (Convite à Escrita):** blocos vazios recém-criados ou aguardando digitação exibem um pulso âmbar acolhedor no bullet. No instante em que o primeiro caractere é digitado, o bullet salta com uma curva elástica para o batimento teal esmeralda.
- **Pulso bioluminescente nos bullet threads:** a linha vertical que liga o pai aos filhos cresce de cima para baixo e, enquanto o pai está em foco, um fluxo de luz bioluminescente percorre continuamente a linha em direção aos descendentes.
- **Halo orbital em blocos-pai (Pre-attentive Branching):** blocos que possuem filhos exibem um anel orbital suave (`.rem-bullet__ring`) mesmo em repouso, permitindo bater o olho e reconhecer imediatamente a profundidade e densidade de cada tópico da árvore.
- **Bullets táteis:** crescem com mola (`cubic-bezier(0.34, 1.56, 0.64, 1)`) ao passar o mouse, "afundam" ao clicar e o bullet do bloco ativo pulsa como um batimento cardíaco.
- **Referências e links elétricos:** cápsulas em azul elétrico vibrante (`#38bdf8` / `#7dd3fc`) com glow suave e sublinhado magnético que entra da esquerda para a direita no hover.
- **Blocos novos:** sobem suavemente ao serem criados (Enter, colar) e os blocos abaixo deslizam em vez de pular.
- **Menus e omnibar:** aparecem com um leve "pop" e os resultados da busca surgem em cascata, 28ms entre si.
- **Controles:** botões com mola e "squish" no clique, botão primário com varredura de luz, checkbox que dá um pop ao marcar, campos com halo de foco.
- **Flashcards:** o cartão é "distribuído" com uma pequena rotação ao entrar, clozes em âmbar brilham no hover.
- **Detalhes:** cursor e seleção na cor do acento, ponto de "Today" respirando, luz ambiente quase imperceptível no fundo.

## Princípios de design

As regras que mantêm o tema vivo sem distrair:

- Movimento é informação: nada anima sem uma ação do usuário.
- Easing assimétrico: chega rápido (feedback), sai devagar (desfoque).
- Apenas `transform`, `opacity` e `box-shadow` são animados, sem custo de layout durante a digitação.
- `prefers-reduced-motion` desativa todas as animações; ficam apenas as cores e o modo foco estático.

## Personalização rápida

No topo de [`theme.css`](./theme.css), estas variáveis ajustam a intensidade:

- `--ad-dim`: opacidade dos blocos fora de foco (padrão `0.4`; use `1` para desligar o modo foco).
- `--ad-t-defocus`: duração da saída de foco (padrão `700ms`).
- `--ad-accent-rgb` e `--ad-amber-rgb`: cores de acento e de memória/ênfase.

## Limitações conhecidas

O RemNote achata os blocos no DOM agrupados por profundidade, então o CSS não consegue reconhecer o "bloco vizinho" nem os descendentes do bloco em foco.
Por isso todos os outros blocos recuam igualmente.

## Como instalar

Duas opções:

1. **Plugin de tema:** em **Settings > Plugins and Themes > Build**, clique em **Upload Theme** e envie `alive-dark-remnote-theme.zip`.
2. **Custom CSS:** `Ctrl + P`, **Custom CSS**, **Add Blank CSS Block** e cole o conteúdo de `theme.css`.

O modo escuro do RemNote precisa estar ativo.

