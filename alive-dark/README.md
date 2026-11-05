# Alive-Dark Theme for RemNote

Um tema escuro que **responde a você**.
Mantém o conforto ergonômico do [ergo-dark](../ergo-dark/) (ardósia quente, texto em pergaminho, acento verde-eucalipto) e adiciona movimento com propósito: cada animação responde a uma ação sua e dura menos de 600ms.

## O que ganha vida

Os efeitos, todos feitos apenas com CSS:

- **Modo foco (profundidade de campo):** enquanto você digita em um bloco, todos os outros recuam (apenas opacidade, o texto continua nítido).
  Passar o mouse sobre um bloco recuado o traz de volta.
  A saída de foco é lenta (700ms, curva `cubic-bezier(0.45, 0, 0.15, 1)`) e a entrada é rápida (140ms), então o olho nunca é puxado bruscamente.
- **Bloco ativo:** holofote em gradiente que deriva lentamente, barra de margem em teal e um brilho que "respira" a cada 5,5s.
  Usa `box-shadow`, então o texto nunca se desloca ao focar.
- **Bullet threads vivos:** a linha de hierarquia cresce de cima para baixo (`scaleY`) e se ilumina ao longo de toda a sub-árvore do bloco em foco ou sob o mouse.
- **Bullets táteis:** crescem com mola (`cubic-bezier(0.34, 1.56, 0.64, 1)`) ao passar o mouse, "afundam" ao clicar e o bullet do bloco ativo pulsa como um batimento lento.
- **Referências e links:** o sublinhado entra da esquerda para a direita no hover.
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
