# Design Patterns — Sinzinger Advocacia (sinzingeradvocacia.com.br)

> **Propósito:** Referência visual para o projeto "Gabriel Direito & Saúde".
> Base de inspiração — **não copiar**, mas usar como referência de estrutura,
> conceitos e padrões que funcionam.

---

## 1. STACK TECNOLÓGICO

| Componente | Tecnologia |
|---|---|
| CMS | WordPress 6.x |
| Tema | Hello Elementor (starter mínimo) |
| Page Builder | Elementor Pro (kit `elementor-kit-7`) |
| Cache | LiteSpeed Cache (CSS otimizado num único arquivo) |
| Scroll suave | Lenis 1.1.16 (`lenis.min.js`, unpkg) |
| Slider | Swiper (via Elementor n-carousel) |
| Fontes | Self-hosted (DM Sans, Metropolis, Libre Baskerville) |
| Template | `elementor_canvas` (full-width, sem header/footer do tema) |
| Transição página | `e-page-transition` (cor de fundo #FFBC7D) |

---

## 2. ESTRUTURA DA PÁGINA (single-page)

**Layout:** Canvas full-width, sem header, sem nav menu tradicional.
**Todas as seções:** Containers flex do Elementor (`--display:flex`).

```
┌─────────────────────────────────────────┐
│            HERO SECTION                 │
│  ┌─────────────────────────────────┐    │
│  │  Logo (image-box)               │    │
│  │  H1: Dr. Gustavo Sinzinger     │    │
│  │  Descrição: "Advogado          │    │
│  │  especializado em Direito da   │    │
│  │  Saúde."                       │    │
│  │  Elemento flutuante (floating) │    │
│  │  (decoração)                   │    │
│  └─────────────────────────────────┘    │
│  (bg: imagem hero full-width)          │
│  (justify-content: flex-end)           │
│  (padding: 2em top)                    │
├─────────────────────────────────────────┤
│       CARDS SECTION (n-carousel)        │
│  ┌──────┐  ┌──────┐  ┌──────┐         │
│  │ Card1│  │ Card2│  │ Card3│  ...    │
│  │ Icon │  │ Icon │  │ Icon │         │
│  │ Box  │  │ Box  │  │ Box  │         │
│  │ Title│  │Title │  │Title │         │
│  │Saiba │  │Saiba │  │Saiba │         │
│  │ mais │  │ mais │  │ mais │         │
│  └──────┘  └──────┘  └──────┘         │
│  (2 slides/linha desktop)              │
│  (1 slide/linha mobile)               │
├─────────────────────────────────────────┤
│     CTA SECTION — Fale conosco         │
│  H2: Fale com o escritório             │
│  H3: Entre em contato                  │
│  (link WhatsApp)                        │
├─────────────────────────────────────────┤
│     CTA SECTION — YouTube              │
│  H2: Acesse meu canal no Youtube       │
│  H3: Acesse agora                       │
│  (link YouTube)                         │
├─────────────────────────────────────────┤
│         FOOTER                          │
│  Divider: gold 1px (opacidade 12%)     │
│  Contato (icon-list)                   │
│  Instagram                              │
│  São Paulo - SP                         │
│  "Desenvolvido por DannyHana"          │
│  (bg: #090706)                          │
└─────────────────────────────────────────┘
```

### Widgets utilizados (contagem)

| Widget | Qtd | Função |
|---|---|---|
| `elementor-widget-icon-box` | 10 | Cards de serviço |
| `elementor-widget-image` | 2 | Logo, decoração |
| `elementor-widget-image-box` | 1 | Hero (logo + título) |
| `elementor-widget-n-carousel` | 1 | Slider de cards |
| `elementor-widget-icon-list` | 2 | Contato, links |
| `elementor-widget-divider` | 1 | Separador footer |
| `elementor-widget-text-editor` | 1 | Texto footer |

---

## 3. PALETA DE CORES

### Cores do kit global (Elementor)

```
--e-global-color-primary:   #FAFAFA   (off-white, bg principal)
--e-global-color-secondary: #272727   (dark gray, quase preto)
--e-global-color-text:      #B6B7B9   (cinza claro, texto)
--e-global-color-accent:    #FDE3A8   (dourado claro, accent)

--e-global-color-257038a:   #0B1421   (navy escuro)
--e-global-color-b6a4a93:   #000C15   (navy quase preto)
--e-global-color-0e9b940:   #495566   (azul-ardósia)
--e-global-color-04afed4:   #06CBC0   (ciano/teal — accent secundário)
--e-global-color-2fc40e6:   #EFD9B3   (creme/dourado)
--e-global-color-8bc8687:   #F5F5F5   (cinza claro bg)
--e-global-color-65fad81:   #BF8F50   (dourado médio)
--e-global-color-65fad81:   #C89B5D   (dourado queimado, scrollbar)
```

### Cores aplicadas (uso real)

| Cor | Uso | Contexto |
|---|---|---|
| `#090706` | Footer | Fundo do footer |
| `rgb(22 21 21 / .4)` | Cards | Fundo dos cards com transparência |
| `backdrop-filter: blur(7.5px)` | Cards | Efeito glassmorphism nos cards |
| `rgb(239 217 179 / .15)` | Cards | Borda dourada sutil (1px) |
| `#FDE3A840` | Cards hover | Borda dourada com 25% opacidade |
| `#CFCFCF` | Cards | Título do card (cinza claro) |
| `#EFD9B320` | Divider | Separador gold com 12% opacidade |
| `#FFBC7D` | Transição | Cor de fundo da transição entre páginas |
| `#383737` | Scrollbar | Track da scrollbar |
| `#C89B5D` | Scrollbar | Thumb da scrollbar (dourado) |
| `#FFFFFF` | Links | Cor dos links (botão padrão Elementor) |
| `#69727D` | Botão | Background padrão do botão Elementor |

---

## 4. SISTEMA TIPOGRÁFICO

### Fontes (self-hosted)

| Fonte | Pesos | Uso | Adicionada |
|---|---|---|---|
| **Libre Baskerville** | 400 | Headings / Primary typography | 2026/02 |
| **Metropolis** | 400, 600, 700 | Body, subheadings, accent | 2025/09 |
| **DM Sans** | 400, 600 | UI elements, complementar | 2026/02 |

### Glossário tipográfico (Elementor)

| Variável | Fonte | Peso | Tamanho | Line-height | Uso |
|---|---|---|---|---|---|
| `--e-global-typography-primary-font-family` | Libre Baskerville | 400 | 2.5rem | 1.3em | Headings (H1-H2) |
| `--e-global-typography-secondary-font-family` | Metropolis | 600 | — | 1.5em | Subheadings, botões |
| `--e-global-typography-text-font-family` | Metropolis | 400 | 1em | 1.5em | Corpo de texto |
| `--e-global-typography-accent-font-family` | Metropolis | 600 | 1em | — | Labels, UPPERCASE |

### Tamanhos aplicados

| Elemento | Fonte | Tamanho | Peso | Line-height |
|---|---|---|---|---|
| H1 (hero) | Libre Baskerville | 1.3rem | 400 | 1.3em |
| H2 (card title) | Metropolis (via kit) | variável | 600 | variável |
| H3 "Saiba mais" | Metropolis | variável | 600 | variável |
| Footer descrição | Metropolis | 0.87em | 400 | 1.5em |
| Hero descrição | (span sbbranco) | — | — | — |

---

## 5. ANIMAÇÕES E TRANSIÇÕES

### @keyframes zoomOutBlur (entrada do hero)

```css
@keyframes zoomOutBlur {
  0%   { transform: scale(1.1); filter: blur(8px); opacity: 0.7; }
  100% { transform: scale(1);  filter: blur(0);   opacity: 1; }
}
```

**Uso:** Imagem de fundo do hero-section.
**Duração:** 1.3s, ease-out, forwards.
**Efeito:** Entrada dramática — zoom out sutil com desfoque inicial.

### @keyframes floating (elemento decorativo)

```css
@keyframes floating {
  0%, 100% { transform: translate(0, 0); }
  50%      { transform: translate(0, 20px); }
}
```

**Uso:** Elemento decorativo flutuante no hero.
**Duração:** 6s, ease-in-out, infinite.
**Efeito:** Movimento suave para cima e para baixo (levitação).

### Card hover

```css
.card:hover {
  border-style: solid;
  border-width: 1px;
  border-color: #FDE3A840;  /* dourado com 25% opacity */
}
```

### Transição padrão Elementor

```css
.elementor-button {
  transition: all 0.3s ease-in-out;
}
```

### Página transition

```css
e-page-transition {
  background-color: #FFBC7D;  /* pêssego */
}
```

### Smooth scroll (Lenis)

```html
<script src="https://unpkg.com/lenis@1.1.16/dist/lenis.min.js"></script>
```

---

## 6. COMPONENTES E PADRÕES DE LAYOUT

### Hero Section

- **Layout:** Flex container, `justify-content: flex-end` (conteúdo alinhado ao fundo)
- **Padding:** 2em top, 0 bottom
- **Background:** Imagem full-width `pagina_bio.webp` (escura, provavelmente foto do escritório)
- **Logo:** image-box widget, `margin-top: 14em`, `text-align: start`
- **Conteúdo:** H1 "Dr. Gustavo Sinzinger" (Libre Baskerville, 1.3rem)
- **Descrição:** "Advogado especializado em Direito da Saúde." (span `sbbranco`)
- **Decoração:** Elemento com `animation: floating 6s ease-in-out infinite`

### Card Section (n-carousel)

- **Tipo:** Swiper carousel (Elementor n-carousel)
- **Slides por linha:** 2 (desktop), 1 (tablet/mobile)
- **Gap entre slides:** 10px
- **z-index:** 999 (sobrepõe hero)
- **Card (icon-box):**
  - `border-radius: 10px`
  - `border: 1px solid rgb(239 217 179 / .15)` (borda dourada sutil)
  - `background: rgb(22 21 21 / .4)` (fundo escuro translúcido)
  - `backdrop-filter: blur(7.5px)` (efeito glassmorphism)
  - **Padding:** 1em (mobile), 2em (desktop)
- **Hover do card:**
  - Borda dourada mais visível: `#FDE3A840`
  - `border-style: solid; border-width: 1px`
- **Título:** `color: #CFCFCF`
- **Ícone:** Elementor icon-box com gap configurável
- **Links:** "Saiba mais" → landing pages /reajuste-abusivo/, /autismo/, /coparticipacao/

### Cards individuais

| Card | Título | Link |
|---|---|---|
| 1 | Reajuste abusivo em planos de saúde | /reajuste-abusivo/ |
| 2 | Negativa de tratamento para autistas | /autismo/ |
| 3 | Cobrança abusiva de coparticipação | /coparticipacao/ |
| 4 | WhatsApp | tintim.link/whatsapp/... |
| 5 | YouTube | youtube.com/@gustavosinzinger |

### CTA Sections

- **Layout:** Mesmo padrão dos cards (icon-box com glassmorphism)
- **Títulos:** "Fale com o escritório Sinzinger Advocacia", "Acesse meu canal no Youtube"
- **Sub-título:** "Entre em contato", "Acesse agora"
- **Links:** WhatsApp (tintim.link), YouTube

### Footer

- **Background:** `#090706` (preto muito escuro)
- **Padding:** 5em top, 3em bottom (desktop), 2em (mobile)
- **Divider:** `solid 1px #EFD9B320` (dourado com 12% opacidade)
- **Conteúdo:** Contato, Instagram, São Paulo - SP, "Desenvolvido por DannyHana"
- **Fonte:** Metropolis, 0.87em, 400
- **Icon-list:** Ícones de 25px, gap vertical 14px (mobile) / 49px (desktop)

### Scrollbar customizada

```css
body::-webkit-scrollbar {
  width: 7px;
}
body::-webkit-scrollbar-track {
  background: #383737;
}
body::-webkit-scrollbar-thumb {
  background: #C89B5D;
  border-radius: 10px;
  border: 1.5px solid #C89B5D;
}
```

---

## 7. DECISÕES DE DESIGN VISUAL

### Atmosfera
- **Escuro e sofisticado** — fundos escuros (#090706, #0B1421, #272727) com
  detalhes em dourado (#FDE3A8, #C89B5D, #EFD9B3)
- **Luxo acessível** — dourado como cor de destaque, sem ser ostensivo
- **Profissional e sério** — tipografia serifada (Libre Baskerville) para
  autoridade, sans-serif (Metropolis) para legibilidade

### Efeitos
- **Glassmorphism** — Cards com fundo translúcido + blur
- **Bordas sutis** — 1px com cor dourada em baixa opacidade
- **Hover minimalista** — Apenas borda mais visível no hover (sem escala,
  sem sombra)
- **Entrada dramática** — Hero com zoomOutBlur
- **Movimento orgânico** — Elemento flutuante (floating)

### Ausências notáveis
- **Sem header/nav menu** — Navegação só pelos cards e links WhatsApp/YouTube
- **Sem box-shadow** — Design flat com bordas, não sombras
- **Sem gradientes** — Cores sólidas ou imagens de fundo
- **Sem footer tradicional** — Apenas informação de contato compacta
- **Sem formulário de contato** — Toda conversão via WhatsApp

---

## 8. RESPONSIVIDADE

### Breakpoints (Elementor)

| Dispositivo | Largura | Mudanças principais |
|---|---|---|
| Desktop | > 1024px | 2 slides carrossel, padding 2em cards |
| Tablet | 768-1024px | Carrossel vira pilha vertical |
| Mobile | < 768px | 1 slide carrossel, padding 1em cards, logo margin 12em top |

### Mobile-first patterns
- Carrossel → empilhamento vertical (`overflow: visible`, `flex-direction: column`)
- Padding reduzido em containers (2em → 1em)
- Margem do logo no hero reduzida (14em → 12em)
- Gap do icon-list reduzido (49px → 14px)

---

## 9. PADRÕES DE CÓDIGO (CSS)

### Variáveis globais do kit
```css
--e-global-color-primary: #FAFAFA;
--e-global-color-secondary: #272727;
--e-global-color-text: #B6B7B9;
--e-global-color-accent: #FDE3A8;
--e-global-typography-primary-font-family: "Libre Baskerville", Sans-serif;
--e-global-typography-secondary-font-family: "Metropolis", Sans-serif;
--e-global-typography-text-font-family: "Metropolis", Sans-serif;
--e-global-typography-accent-font-family: "Metropolis", Sans-serif;
```

### Container flex (Elementor)
```css
--display: flex;
--flex-direction: column;
--container-widget-width: 100%;
--container-widget-height: initial;
--container-widget-flex-grow: 0;
--container-widget-align-self: initial;
--flex-wrap-mobile: wrap;
```

---

## 10. RECOMENDAÇÕES PARA O GABRIEL DIREITO & SAÚDE

> **Princípio:** Inspirar-se na estrutura e conceitos, não copiar o visual.

### O que manter
- ✅ Single-page com hero impactante + cards de serviço + CTA + footer
- ✅ Efeito glassmorphism nos cards (funciona bem)
- ✅ Scroll suave (Lenis) — experiência premium
- ✅ Entrada com zoomOutBlur ou similar no hero
- ✅ Paleta escura + cor de destaque (mas escolher sua própria combinação)
- ✅ Tipografia: serifada para headings + sans-serif para corpo

### O que adaptar
- 🔄 **Paleta de cores:** escolher cores próprias (sugestão: verde saúde + azul confiança)
- 🔄 **Fontes:** Libre Baskerville pode ser substituída por outra serifada
- 🔄 **Cards:** Substituir carrossel por grid fixo (mais acessível, indexável)
- 🔄 **Botões:** Sinzinger não tem CTAs destacados — adicionar botão primário
- 🔄 **Header:** Adicionar navegação superior (Sinzinger não tem)
- 🔄 **Formulário:** Adicionar formulário de contato (Sinzinger só WhatsApp)

### O que evitar
- ❌ Copiar o dourado (#FDE3A8, #C89B5D) — é a identidade visual do Sinzinger
- ❌ Copiar a foto do hero ou layout exato
- ❌ Copiar textos específicos ("Dr. Gustavo Sinzinger", etc.)
- ❌ Copiar a estrutura de cores do kit Elementor

---

## 11. ARQUIVOS FONTE

- `index.html` — HTML completo da página (76KB)
- `main.css` — CSS otimizado (LiteSpeed)
- `design-patterns-sinzinger.md` — este documento

---

*Extraído em 31/08/2026 via análise de HTML + CSS do site sinzingeradvocacia.com.br.*
*Chrome indisponível no ambiente — extração via curl + análise estática.*