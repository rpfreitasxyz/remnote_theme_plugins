# Ergo-Dark Theme for RemNote

Um tema escuro cientificamente calibrado com base em ergonomia visual, óptica fisiológica e teoria da carga cognitiva para sessões prolongadas de leitura, escrita e repetição espaçada no RemNote.
Cada decisão cromática foi projetada para eliminar o efeito de halação (borramento luminoso), reduzir a fadiga do músculo ciliar (astenopia digital) e facilitar o processamento pré-atentivo da hierarquia de notas.

## Fundamentos de Teoria das Cores e Ergonomia Visual

O desenvolvimento do Ergo-Dark baseia-se nos seguintes princípios científicos:

- **Prevenção de Halação e Aberração Esférica (CIELAB $L^* \approx 12$):** Contrastes extremos de 21:1 (`#FFFFFF` sobre `#000000`) causam o efeito de irradiação (o texto claro parece "vazar" sobre o fundo escuro), especialmente em usuários com astigmatismo devido à dilatação pupilar. O Ergo-Dark utiliza uma superfície em ardósia quente (`#1c1e20`) combinada com texto em pergaminho suave (`#d8d4cb`), atingindo uma razão de contraste de ~10.8:1 (WCAG AAA / APCA $L_c \approx 85$), ponto ideal para leitura foveal sem ofuscamento.
- **Zero Aberração Cromática Longitudinal (Pico de Sensibilidade Retiniana em 510–560nm):** A luz azul de onda curta (~450nm) foca antes da retina, obrigando o músculo ciliar a reacomodar o foco constantemente ao ler links azuis saturados sobre fundo escuro. O Ergo-Dark substitui o azul saturado por **Verde-Eucalipto / Celadon (`#7ec4b6`)** e **Sálvia Botânica (`#a3be8c`)**, comprimentos de onda situados no pico de eficiência luminosa fotópica e mesópica do olho humano.
- **Redução da Carga Cognitiva Extrínseca (Sweller & Treisman):** A barra lateral possui luminância levemente inferior (`#16181a`) ao editor central (`#1c1e20`), criando um efeito de vinheta periférica que mantém a atenção ancorada no texto. Elementos semânticos utilizam codificação pré-atentiva distinta: negrito em areia dourada (`#e5c890`), itálico em sálvia (`#a3be8c`) e lacunas de memória (clozes) em âmbar quente (`#dfa86a`).
- **Destaques Iso-Luminantes (Munsell):** As 6 cores de marcação foram equalizadas em luminosidade perceptual e baixa saturação para evitar pós-imagens na retina e fadiga por contraste simultâneo.

## Paleta de Cores Calibrada

| Elemento | Hexadecimal | Função Ergonômica |
| :--- | :--- | :--- |
| Background Editor | `#1c1e20` | Ardósia quente ($L^* \approx 12$) anti-halação e anti-astigmatismo |
| Background Sidebar | `#16181a` | Vinheta periférica para ancorar o foco no documento central |
| Background Elevated | `#232629` | Cartões de flashcard, popups e omnibar com separação suave |
| Texto Principal | `#d8d4cb` | Pergaminho quente (~82% refletância, contraste ~10.8:1 sem brilho azul) |
| Títulos (H1–H3) | `#ece8df` | Marfim suave para hierarquia estrutural sem ofuscamento |
| Negrito (`<strong>`) | `#e5c890` | Areia dourada para escaneamento rápido de conceitos-chave |
| Itálico (`<em>`) | `#a3be8c` | Sálvia botânica para diferenciação semântica suave |
| Links e Âncoras | `#84c5b8` | Eucalipto/Celadon (525nm) de foco retiniano imediato |
| Clozes e Delimitadores | `#dfa86a` | Âmbar ocre para ativação de memória e recordação ativa |
| Bullet Threading | `#33383d` → `#7ec4b6` | Guia espacial discreta em repouso e luminosa no ramo ativo |

## Como Instalar no RemNote

Você pode aplicar o tema por qualquer um dos dois métodos:

### 1. Upload como Plugin de Tema

Os passos para instalar o pacote compactado:

1. Baixe o arquivo `ergo-dark-remnote-theme.zip` desta pasta.
2. No RemNote, acesse **Settings > Plugins and Themes**.
3. Clique na aba **Build**.
4. Clique em **Upload Theme** e selecione o arquivo `.zip`.
5. Certifique-se de que o modo escuro está ativo (**Settings > Theme > Dark**).

### 2. Pelo Powerup Custom CSS

Os passos para colar o código diretamente:

1. No RemNote, pressione `Ctrl + P` (ou `Cmd + P`) e busque por **Custom CSS**.
2. Clique em **Add Blank CSS Block**.
3. Copie o conteúdo de `theme.css` desta pasta e cole no bloco.
4. Dê o nome "Ergo-Dark" ao bloco e ative-o.

## Licença

Distribuído sob a licença MIT.
Consulte o arquivo `LICENSE` na raiz do repositório.
