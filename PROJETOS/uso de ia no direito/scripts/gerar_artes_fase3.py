#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as artes do plano de publicação Instagram — FASE 3 (Autoridade).

Sistema visual EDITORIAL (evolução do Dossiê): grid 12 colunas, alinhamento à
esquerda, etiqueta de protocolo §0X · CATEGORIA, numeração de slide gigante em
AMBER, painel de prova (PAPER com hairline) e rodapé fixo com fio do protocolo
indicando progresso do carrossel.

Saída: instagram-imagens-fase3/
"""

import os
from PIL import Image, ImageDraw, ImageFont

ROOT = "/media/mascarenhas/01D7475AEEEB8480/segundo-cerebro/Segundo-Cerebro/PROJETOS/uso de ia no direito"
FONTS = os.path.join(ROOT, ".claude/skills/canvas-design/canvas-fonts")
OUT = os.path.join(ROOT, "instagram-imagens-fase3")

# ----------------------------------------------------------------- tokens
INK = "#191d30"        # fundo / autoridade
PAPER = "#f4f3ee"      # papel / prova
ORANGE = "#f16520"     # gesto de ação
INK_NAVY = "#2b3a67"   # hierarquia secundária / terminal
AMBER = "#e8a33d"      # destaque editorial / numeração
RED = "#fbecea"
BLUE = "#eef1fb"
GREEN = "#ecf6f0"
MUTED = "#9aa0b8"      # secundário sobre escuro
BODY_LT = "#b9bed8"    # corpo de texto sobre escuro (mais legível que MUTED)
HAIR = "#31374f"       # filetes sobre escuro
WM = "#1e2338"         # marca d'água §
DARK_MUTED = "#5a5f75" # texto secundário sobre painéis claros
PANEL_BORDER = "#d3d3d1"  # INK a 15% sobre PAPER
TERM_BG = "#26345c"    # fundo do painel terminal (navy um tom abaixo)

BRAND = "IA NA ADVOCACIA"
CTA = "CONHEÇA O SITE — LINK NA BIO"

# ----------------------------------------------------------------- fonts
F = {}
VARIABLE = {
    "BricolageGrotesque-Bold.ttf":    ("Bricolage-VF.ttf", "Bold"),
    "BricolageGrotesque-Regular.ttf": ("Bricolage-VF.ttf", "Regular"),
    "WorkSans-Bold.ttf":              ("WorkSans-VF.ttf", "Bold"),
    "WorkSans-Regular.ttf":           ("WorkSans-VF.ttf", "Regular"),
}

def font(name, size):
    key = (name, size)
    if key not in F:
        if name in VARIABLE:
            fname, inst = VARIABLE[name]
            f = ImageFont.truetype(os.path.join(FONTS, fname), size)
            f.set_variation_by_name(inst)
            F[key] = f
        else:
            F[key] = ImageFont.truetype(os.path.join(FONTS, name), size)
    return F[key]

GROT_B = "BricolageGrotesque-Bold.ttf"
MONO = "IBMPlexMono-Regular.ttf"
MONO_B = "IBMPlexMono-Bold.ttf"
SERIF_I = "IBMPlexSerif-Italic.ttf"
SERIF = "IBMPlexSerif-Regular.ttf"
SANS = "WorkSans-Regular.ttf"
SANS_B = "WorkSans-Bold.ttf"

# ----------------------------------------------------------------- helpers
def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def wrap(d, text, fnt, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def tracked(d, xy, text, fnt, fill, tracking=5, anchor_right=None, canvas_w=None):
    total = sum(d.textlength(c, font=fnt) + tracking for c in text) - tracking
    x, y = xy
    if anchor_right:
        x = canvas_w - x - total
    for c in text:
        d.text((x, y), c, font=fnt, fill=fill)
        x += d.textlength(c, font=fnt) + tracking
    return total

def dashed_line(d, x0, y, x1, color, width=2, dash=10, gap=8):
    x = x0
    while x < x1:
        d.line([(x, y), (min(x + dash, x1), y)], fill=color, width=width)
        x += dash + gap

def progress_line(d, x0, y, x1, page, total):
    """Fio do protocolo: porção sólida cresce da esquerda → direita (progresso)."""
    frac = max(0.0, min(1.0, page / float(total)))
    fx = x0 + (x1 - x0) * frac
    d.line([(x0, y), (fx, y)], fill=AMBER, width=3)
    dashed_line(d, fx, y, x1, HAIR, width=2)
    d.ellipse([fx - 6, y - 6, fx + 6, y + 6], fill=AMBER)

def rounded(d, box, fill, radius=24, outline=None, width=2):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def arrow(d, x, y, ln, color, w=3):
    d.line([(x, y), (x + ln, y)], fill=color, width=w)
    d.line([(x + ln - 14, y - 9), (x + ln, y)], fill=color, width=w)
    d.line([(x + ln - 14, y + 9), (x + ln, y)], fill=color, width=w)

def watermark(img, x, y, size=720):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    dl = ImageDraw.Draw(layer)
    dl.text((x, y), "§", font=font("Gloock-Regular.ttf", size), fill=WM)
    img.paste(Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB"), (0, 0))

# ----------------------------------------------------------------- mini icons
def mini_icon(d, kind, cx, cy, s, color):
    w = 3
    if kind == "search":
        d.ellipse([cx - s, cy - s, cx + s, cy + s], outline=color, width=w)
        d.line([cx + s * 0.55, cy + s * 0.55, cx + s, cy + s], fill=color, width=w + 1)
    elif kind == "doc":
        d.rounded_rectangle([cx - s, cy - s, cx + s, cy + s], radius=4, outline=color, width=w)
        for i in range(3):
            yy = cy - s * 0.45 + i * s * 0.45
            d.line([cx - s * 0.55, yy, cx + s * 0.55, yy], fill=color, width=w)
    elif kind == "contract":
        d.rounded_rectangle([cx - s, cy - s, cx + s, cy + s], radius=4, outline=color, width=w)
        d.line([cx + s * 0.2, cy - s, cx + s, cy - s * 0.2], fill=color, width=w)
        for i in range(2):
            yy = cy + s * 0.05 + i * s * 0.45
            d.line([cx - s * 0.55, yy, cx + s * 0.35, yy], fill=color, width=w)
    elif kind == "lock":
        d.rounded_rectangle([cx - s * 0.7, cy - s * 0.05, cx + s * 0.7, cy + s], radius=4, outline=color, width=w)
        d.arc([cx - s * 0.45, cy - s * 0.8, cx + s * 0.45, cy + s * 0.1], 180, 360, fill=color, width=w)
    elif kind == "scale":
        d.line([cx, cy - s, cx, cy + s], fill=color, width=w)
        d.line([cx - s * 0.95, cy - s * 0.45, cx + s * 0.95, cy - s * 0.45], fill=color, width=w)
        d.ellipse([cx - s * 0.3, cy + s * 0.75, cx + s * 0.3, cy + s * 1.25], fill=color)
        d.line([cx - s * 0.95, cy - s * 0.45, cx - s * 0.95, cy + s * 0.15], fill=color, width=w)
        d.line([cx + s * 0.95, cy - s * 0.45, cx + s * 0.95, cy + s * 0.15], fill=color, width=w)
        d.arc([cx - s * 1.15, cy - s * 0.05, cx - s * 0.75, cy + s * 0.4], 0, 180, fill=color, width=w)
        d.arc([cx + s * 0.75, cy - s * 0.05, cx + s * 1.15, cy + s * 0.4], 0, 180, fill=color, width=w)
    elif kind == "check":
        d.line([cx - s * 0.75, cy, cx - s * 0.1, cy + s * 0.6], fill=color, width=w + 1)
        d.line([cx - s * 0.1, cy + s * 0.6, cx + s * 0.8, cy - s * 0.65], fill=color, width=w + 1)
    elif kind == "warn":
        d.polygon([(cx, cy - s), (cx + s * 0.9, cy + s * 0.75), (cx - s * 0.9, cy + s * 0.75)],
                  outline=color, width=w)
        d.line([cx, cy - s * 0.25, cx, cy + s * 0.25], fill=color, width=w)
        d.ellipse([cx - 3, cy + s * 0.42, cx + 3, cy + s * 0.52], fill=color)
    elif kind == "quote":
        d.text((cx - s * 0.9, cy - s * 1.15), "\u201c", font=font(SERIF_I, int(s * 2.4)), fill=color)
    elif kind == "steps":
        for i in range(3):
            bx = cx - s + i * s * 0.95
            d.rectangle([bx, cy + s * 0.5 - i * s * 0.45, bx + s * 0.75, cy + s * 0.7 - i * s * 0.45],
                        outline=color, width=w)
    elif kind == "chat":
        d.rounded_rectangle([cx - s, cy - s * 0.7, cx + s, cy + s * 0.5], radius=6, outline=color, width=w)
        d.polygon([(cx - s * 0.3, cy + s * 0.5), (cx - s * 0.05, cy + s * 0.9), (cx + s * 0.1, cy + s * 0.5)],
                  fill=color)
        for i in range(2):
            d.line([cx - s * 0.45 + i * s * 0.5, cy - s * 0.1, cx - s * 0.2 + i * s * 0.5, cy - s * 0.1],
                   fill=color, width=w)

# ----------------------------------------------------------------- chrome
def canvas(W, H):
    img = Image.new("RGB", (W, H), INK)
    return img, ImageDraw.Draw(img)

def save(img, rel):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, "PNG")
    print("  ok", rel)

FW, FH, M = 1080, 1350, 100   # feed

def masthead(d, W, m, y, post_num, category, accent=AMBER):
    d.text((m, y - 6), "§", font=font(SERIF, 32), fill=accent)
    tracked(d, (m + 40, y + 2), f"{post_num:02d} · {category}", font(MONO, 24), accent, tracking=7)
    yh = y + 46
    d.line([(m, yh), (W - m, yh)], fill=HAIR, width=2)
    return yh + 42

def giant_num(d, m, y, n, size=196, color=AMBER):
    f = font(MONO_B, size)
    txt = f"{n:02d}"
    d.text((m, y), txt, font=f, fill=color)
    return d.textlength(txt, font=f)

def new_slide(post_num, category, slide_num, accent=AMBER, wm=(700, 720)):
    img, d = canvas(FW, FH)
    watermark(img, *wm)
    d = ImageDraw.Draw(img)
    y = masthead(d, FW, M, M, post_num, category, accent)
    num_w = giant_num(d, M, y + 4, slide_num)
    cx = M + num_w + 52
    cw = FW - M - cx
    return img, d, cx, y + 4, cw

def footer(d, W, H, m, page, total, mode):
    yl = H - 168
    d.line([(m, yl), (W - m, yl)], fill=HAIR, width=2)
    d.text((m, yl + 30), "§", font=font(SERIF, 26), fill=AMBER)
    tracked(d, (m + 32, yl + 36), BRAND, font(MONO, 21), MUTED, tracking=5)
    tracked(d, (m, yl + 36), f"{page:02d}/{total:02d}", font(MONO, 21), MUTED,
            tracking=4, anchor_right=True, canvas_w=W)
    if mode == "cta":
        f = font(MONO_B, 27)
        tw = sum(d.textlength(c, font=f) + 5 for c in CTA) - 5
        pw, ph = tw + 80, 68
        x0 = (W - pw) / 2
        rounded(d, [x0, yl + 78, x0 + pw, yl + 78 + ph], AMBER, radius=34)
        tracked(d, (x0 + 40, yl + 78 + ph / 2 - 14), CTA, f, INK, tracking=5)
    else:  # swipe
        f = font(MONO_B, 23)
        lab = "ARRASTE"
        tw = sum(d.textlength(c, font=f) + 4 for c in lab) - 4
        ax = W - m - 56
        tracked(d, (ax - 18 - tw, yl + 102 - 12), lab, f, PAPER, tracking=4)
        arrow(d, ax, yl + 102, 52, AMBER, w=4)
    progress_line(d, m, H - 38, W - m, page, total)

# ----------------------------------------------------------------- text blocks
def headline_box(d, x, y, w, text, size=62, color=PAPER, leading=1.1, fnt=GROT_B):
    f = font(fnt, size)
    for ln in wrap(d, text, f, w):
        d.text((x, y), ln, font=f, fill=color)
        y += int(size * leading)
    return y

def body_box(d, x, y, w, text, size=33, color=BODY_LT, leading=1.44, fnt=SANS):
    f = font(fnt, size)
    for ln in wrap(d, text, f, w):
        d.text((x, y), ln, font=f, fill=color)
        y += int(size * leading)
    return y

def proof_panel(d, x, y, w, blocks, icon_kind=None):
    """Painel de prova: PAPER com borda hairline, ícone à esquerda, texto à direita.
    blocks: list de {"text","style"(bold|body|mono|quote),"size","color"}."""
    pad = 38
    icon_col = 66 if icon_kind else 0
    inner_w = w - 2 * pad - icon_col
    rendered = []
    for b in blocks:
        style = b.get("style", "body")
        size = b.get("size", 34)
        if style == "bold":
            f, col = font(GROT_B, size), b.get("color", INK)
            lh = int(size * 1.16)
        elif style == "mono":
            f, col = font(MONO, size), b.get("color", INK)
            lh = int(size * 1.16)
        elif style == "quote":
            f, col = font(SERIF_I, size), b.get("color", INK)
            lh = int(size * 1.34)
        else:
            f, col = font(SANS, size), b.get("color", DARK_MUTED)
            lh = int(size * 1.44)
        lines = wrap(d, b["text"], f, inner_w)
        rendered.append((lines, f, col, lh))
    total_h = sum(len(ln) * lh for ln, f, col, lh in rendered) + 12 * (len(rendered) - 1)
    ph = pad * 2 + total_h
    rounded(d, [x, y, x + w, y + ph], PAPER, radius=22)
    d.rounded_rectangle([x, y, x + w, y + ph], radius=22, outline=PANEL_BORDER, width=2)
    tx = x + pad + icon_col
    if icon_kind:
        mini_icon(d, icon_kind, x + pad + 16, y + pad + 16, 17, INK)
    cy = y + pad
    for lines, f, col, lh in rendered:
        for ln in lines:
            d.text((tx, cy), ln, font=f, fill=col)
            cy += lh
        cy += 12
    return y + ph

def terminal_panel(d, x, y, w, text, title="prompt.txt"):
    """Painel estilo terminal: navy, mono, barra de título com dots."""
    pad = 34
    bar_h = 46
    f = font(MONO, 31)
    inner_w = w - 2 * pad
    lines = wrap(d, text, f, inner_w)
    lh = int(31 * 1.5)
    ph = bar_h + pad + len(lines) * lh + pad
    rounded(d, [x, y, x + w, y + ph], TERM_BG, radius=20)
    d.rounded_rectangle([x, y, x + w, y + ph], radius=20, outline=HAIR, width=2)
    for i, c in enumerate(["#f16520", "#e8a33d", "#7d8aa8"]):
        d.ellipse([x + 24 + i * 26, y + 17, x + 24 + i * 26 + 12, y + 17 + 12], fill=c)
    tracked(d, (x + 24 + 3 * 26 + 20, y + 21), title, font(MONO, 19), "#8a92b0", tracking=3)
    cy = y + bar_h + pad
    for i, ln in enumerate(lines):
        d.text((x + pad, cy), ln, font=f, fill=PAPER)
        cy += lh
    return y + ph

def quote_panel(d, x, y, w, text, size=36):
    """Painel de destaque AMBER com citação serif italic em INK."""
    pad = 42
    f = font(SERIF_I, size)
    lines = wrap(d, text, f, w - 2 * pad)
    lh = int(size * 1.34)
    ph = pad * 2 + len(lines) * lh + 12
    rounded(d, [x, y, x + w, y + ph], AMBER, radius=22)
    d.text((x + pad - 8, y - 6), "\u201c", font=font(SERIF_I, int(size * 1.9)), fill=INK)
    cy = y + pad + 14
    for ln in lines:
        d.text((x + pad + 8, cy), ln, font=f, fill=INK)
        cy += lh
    return y + ph

# ================================================================ POST 1 — GUIA
def p1():
    base = "post1-guia-ia"
    T = 6
    # s1 capa
    img, d, cx, cy, cw = new_slide(1, "GUIA", 1)
    y = headline_box(d, cx, cy, cw, "Qual IA usar para cada tarefa do seu escritório?", 68, PAPER)
    y += 28
    y = proof_panel(d, cx, y, cw, [
        {"text": "Adoção de IA em escritórios", "style": "body", "size": 30},
        {"text": "11% (2023) → 30% (2024). Quase triplicou.", "style": "bold", "size": 38},
    ], icon_kind="search")
    footer(d, FW, FH, M, 1, T, "swipe"); save(img, f"{base}/slide-1.png")

    def task(n, task, tools, expl, icon):
        img, d, cx, cy, cw = new_slide(1, "GUIA", n)
        y = headline_box(d, cx, cy, cw, task, 60, PAPER)
        y += 30
        y = proof_panel(d, cx, y, cw, [{"text": tools, "style": "bold", "size": 40}], icon_kind=icon)
        y += 26
        y = body_box(d, cx, y, cw, expl, 33)
        footer(d, FW, FH, M, n, T, "swipe"); save(img, f"{base}/slide-{n}.png")

    task(2, "Pesquisar e resumir processos", "JusIA, Locus.IA, ChatGPT Team.",
         "Legaltechs nacionais têm jurisprudência real indexada. Para resumo, o Team protege os dados (DPA). O gratuito, não.",
         "search")
    task(3, "Estruturar petição e peça", "JUIT, Lawdeck, ChatADV.",
         "Feitas para o direito brasileiro, com base jurídica nacional. Reduzem o risco de alucinação na origem.",
         "doc")
    task(4, "Analisar contrato e cláusulas de risco", "Claude, Copilot.",
         "Janela de contexto longa lê contratos inteiros. Use versão empresarial com DPA e anonimize as partes.",
         "contract")
    task(5, "Sigilo máximo (offline)", "LM Studio, Ollama.",
         "A IA roda no seu PC, sem internet. O dado do cliente nunca sai da máquina. O custo é a configuração técnica.",
         "lock")

    # s6 CTA
    img, d, cx, cy, cw = new_slide(1, "GUIA", 6)
    y = headline_box(d, cx, cy, cw, "A ferramenta não te protege da OAB. O método sim.", 60, AMBER)
    y += 28
    y = body_box(d, cx, y, cw,
                 "Versão gratuita treina com seus dados = Art. 34 do Estatuto + LGPD. O guia completo de escolha está no site.",
                 34)
    footer(d, FW, FH, M, 6, T, "cta"); save(img, f"{base}/slide-6.png")

# ================================================================ POST 2 — MÉTODO
def p2():
    base = "post2-prompts"
    T = 6
    # s1 capa
    img, d, cx, cy, cw = new_slide(2, "MÉTODO", 1)
    y = headline_box(d, cx, cy, cw, "3 prompts testados para a sua rotina.", 66, PAPER)
    y += 22
    y = headline_box(d, cx, y, cw, "(Não são mágicos. São estruturados.)", 34, BODY_LT, leading=1.2, fnt=SERIF_I)
    footer(d, FW, FH, M, 1, T, "swipe"); save(img, f"{base}/slide-1.png")

    def prompt_slide(n, title, prompt, why):
        img, d, cx, cy, cw = new_slide(2, "MÉTODO", n)
        y = headline_box(d, cx, cy, cw, title, 56, PAPER)
        y += 26
        y = terminal_panel(d, cx, y, cw, prompt)
        y += 22
        y = body_box(d, cx, y, cw, why, 32)
        footer(d, FW, FH, M, n, T, "swipe"); save(img, f"{base}/slide-{n}.png")

    prompt_slide(2, "Prompt do Resumo",
                 "Cole o acórdão abaixo. Devolva: (1) tese central, (2) fundamento legal citado, (3) dispositivo. Não invente nada fora do texto.",
                 "Funciona porque tranca a IA no texto que você forneceu.")
    prompt_slide(3, "Prompt da Estrutura de Contestação",
                 "A partir dos fatos abaixo, monte o ESQUELETO da contestação: teses em tópicos. Não cite jurisprudência — eu forneço as fontes.",
                 "Você pede estrutura, não “jurisprudência”. Isso elimina o berço da alucinação.")
    prompt_slide(4, "Prompt da Revisão de Cláusulas",
                 "Liste cláusulas potencialmente abusivas no contrato abaixo, com base na LGPD e no CDC. Aponte o risco, não decida por mim.",
                 "A IA aponta; o advogado decide. Responsabilidade técnica continua sua.")

    # s5 regra de ouro
    img, d, cx, cy, cw = new_slide(2, "MÉTODO", 5)
    y = headline_box(d, cx, cy, cw, "A regra de ouro.", 60, PAPER)
    y += 28
    y = quote_panel(d, cx, y, cw,
                    "Nunca peça para a IA citar jurisprudência. Cole a decisão real e diga: use EXCLUSIVAMENTE esta fonte.", 34)
    y += 22
    y = body_box(d, cx, y, cw, "Inverter a lógica é o que protege o Art. 77 do CPC.", 33)
    footer(d, FW, FH, M, 5, T, "swipe"); save(img, f"{base}/slide-5.png")

    # s6 CTA
    img, d, cx, cy, cw = new_slide(2, "MÉTODO", 6)
    y = headline_box(d, cx, cy, cw, "Prompt bom é estrutura, não feitiço.", 60, AMBER)
    y += 28
    y = body_box(d, cx, y, cw, "O kit com os prompts validados, prontos para copiar e adaptar, está no site.", 34)
    footer(d, FW, FH, M, 6, T, "cta"); save(img, f"{base}/slide-6.png")

# ================================================================ POST 3 — PASSO A PASSO
def p3():
    base = "post3-peticao-7-passos"
    T = 6
    # s1 capa
    img, d, cx, cy, cw = new_slide(3, "PASSO A PASSO", 1)
    y = headline_box(d, cx, cy, cw, "Do processo de 500 páginas à petição em 7 passos.", 62, PAPER)
    y += 22
    y = headline_box(d, cx, y, cw, "(Com método. Sem alucinação.)", 34, BODY_LT, leading=1.2, fnt=SERIF_I)
    footer(d, FW, FH, M, 1, T, "swipe"); save(img, f"{base}/slide-1.png")

    def steps_slide(n, title, blocks, icon="steps"):
        img, d, cx, cy, cw = new_slide(3, "PASSO A PASSO", n)
        y = headline_box(d, cx, cy, cw, title, 56, PAPER)
        y += 28
        y = proof_panel(d, cx, y, cw, blocks, icon_kind=icon)
        footer(d, FW, FH, M, n, T, "swipe"); save(img, f"{base}/slide-{n}.png")

    steps_slide(2, "Passos 1–2: Preparo", [
        {"text": "1. Anonimize", "style": "bold", "size": 35},
        {"text": "Troque nome, CPF e valores por [CLIENTE], [CPF], [VALOR] (LGPD + Art. 34).", "style": "body", "size": 31},
        {"text": "2. Pesquise você mesmo", "style": "bold", "size": 35},
        {"text": "A jurisprudência você busca e valida — nunca delegue à IA.", "style": "body", "size": 31},
    ], icon="lock")

    # s3 prompt com trava (terminal)
    img, d, cx, cy, cw = new_slide(3, "PASSO A PASSO", 3)
    y = headline_box(d, cx, cy, cw, "Passo 3: O prompt com trava.", 56, PAPER)
    y += 26
    y = terminal_panel(d, cx, y, cw,
                       "Cole a decisão real. Instrua: “Use EXCLUSIVAMENTE esta fonte. Não invente números de processo, relator ou ementa.”")
    y += 22
    y = body_box(d, cx, y, cw, "A trava anti-alucinação é o coração do método.", 33)
    footer(d, FW, FH, M, 3, T, "swipe"); save(img, f"{base}/slide-3.png")

    steps_slide(4, "Passos 4–5: Estrutura e revisão", [
        {"text": "4. Peça o esqueleto", "style": "bold", "size": 35},
        {"text": "Teses em tópicos, não o texto final.", "style": "body", "size": 31},
        {"text": "5. Revisão humana integral", "style": "bold", "size": 35},
        {"text": "100% sua, linha por linha.", "style": "body", "size": 31},
    ], icon="doc")

    steps_slide(5, "Passos 6–7: Validação e assinatura", [
        {"text": "6. Confira cada citação", "style": "bold", "size": 35},
        {"text": "Contra a fonte original, sempre.", "style": "body", "size": 31},
        {"text": "7. Assine com responsabilidade", "style": "bold", "size": 35},
        {"text": "O dever de veracidade (Art. 77, CPC) é de quem assina.", "style": "body", "size": 31},
    ], icon="check")

    # s6 CTA
    img, d, cx, cy, cw = new_slide(3, "PASSO A PASSO", 6)
    y = headline_box(d, cx, cy, cw, "A IA escreve com você. Nunca por você.", 60, AMBER)
    y += 28
    y = body_box(d, cx, y, cw, "Checklist completo + prompt anti-alucinação no site.", 34)
    footer(d, FW, FH, M, 6, T, "cta"); save(img, f"{base}/slide-6.png")

# ================================================================ POST 4 — CASO REAL (duotone)
def draw_duotone_bg(img, d, W, H):
    top = hex_to_rgb(INK)
    bot = (32, 25, 42)
    for i in range(H):
        t = i / H
        d.line([(0, i), (W, i)],
               fill=tuple(int(top[k] + (bot[k] - top[k]) * t) for k in range(3)))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gx, gy = W * 0.74, H * 0.42
    for r in range(580, 30, -16):
        a = int(32 * (1 - r / 580))
        gd.ellipse([gx - r, gy - r, gx + r, gy + r], fill=(232, 163, 61, a))
    img.paste(Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB"), (0, 0))

def draw_desk_silhouette(d):
    AM = "#e8a33d"
    AM2 = "#b9762a"
    # pastas empilhadas (direita)
    d.rounded_rectangle([660, 372, 820, 568], radius=8, fill=AM2)
    d.rounded_rectangle([692, 340, 852, 540], radius=8, fill=AM)
    d.rectangle([712, 322, 752, 342], fill=AM)
    for i in range(3):
        d.line([712, 404 + i * 34, 822, 404 + i * 34], fill=INK, width=4)
    # balança (geométrica) inferior direita
    sx, sy = 840, 792
    d.line([sx, sy - 150, sx, sy + 40], fill=AM, width=6)
    d.line([sx - 120, sy - 110, sx + 120, sy - 110], fill=AM, width=6)
    d.ellipse([sx - 26, sy + 30, sx + 26, sy + 82], fill=AM)
    d.line([sx - 120, sy - 110, sx - 120, sy - 50], fill=AM, width=5)
    d.line([sx + 120, sy - 110, sx + 120, sy - 50], fill=AM, width=5)
    d.arc([sx - 160, sy - 70, sx - 80, sy - 10], 0, 180, fill=AM, width=6)
    d.arc([sx + 80, sy - 70, sx + 160, sy - 10], 0, 180, fill=AM, width=6)
    # linha da mesa
    d.line([540, sy + 96, 1000, sy + 96], fill=AM2, width=6)

def p4():
    img, d = canvas(FW, FH)
    draw_duotone_bg(img, d, FW, FH)
    d = ImageDraw.Draw(img)
    draw_desk_silhouette(d)
    watermark(img, 120, 950, 560)
    d = ImageDraw.Draw(img)
    y = masthead(d, FW, M, M, 4, "CASO REAL", AMBER)
    y += 26
    y = headline_box(d, M, y, 540, "Ele pediu à IA: \u201ccite jurisprudência\u201d.", 54, PAPER)
    y += 16
    y = headline_box(d, M, y, 540, "A IA inventou. Ele foi multado.", 54, AMBER)
    y += 30
    y = proof_panel(d, M, y, 540, [{"text":
        "Decisão judicial apontou litigância de má-fé e ofensa à dignidade da Justiça em petições com conteúdo jurídico inverídico gerado por IA.",
        "style": "quote", "size": 29}], icon_kind="quote")
    footer(d, FW, FH, M, 1, 1, "cta")
    save(img, "post4-caso-real/feed.png")

# ================================================================ POST 5 — REGULAÇÃO
def p5():
    base = "post5-oab-4-pilares"
    T = 6
    # s1 capa
    img, d, cx, cy, cw = new_slide(5, "REGULAÇÃO", 1)
    y = headline_box(d, cx, cy, cw, "A OAB EXIGE isso de você.", 70, PAPER)
    y += 20
    y = headline_box(d, cx, y, cw, "(Recomendação 001/2024, em 4 pilares.)", 34, BODY_LT, leading=1.2, fnt=SERIF_I)
    footer(d, FW, FH, M, 1, T, "swipe"); save(img, f"{base}/slide-1.png")

    def pilar(n, title, text, icon):
        img, d, cx, cy, cw = new_slide(5, "REGULAÇÃO", n)
        y = headline_box(d, cx, cy, cw, title, 52, PAPER, leading=1.12)
        y += 28
        y = proof_panel(d, cx, y, cw, [{"text": text, "style": "body", "size": 34}], icon_kind=icon)
        footer(d, FW, FH, M, n, T, "swipe"); save(img, f"{base}/slide-{n}.png")

    pilar(2, "Pilar 1 — Legislação Aplicável",
          "LGPD (Lei 13.709/2018) e o Estatuto (Lei 8.906/1994) continuam valendo — inclusive para o uso de IA. A tecnologia não suspende o dever legal.",
          "doc")
    pilar(3, "Pilar 2 — Confidencialidade e Privacidade",
          "Sigilo como dever absoluto (Art. 34). Anonimização obrigatória. O cliente não pode se tornar “inadvertidamente identificável”.",
          "lock")
    pilar(4, "Pilar 3 — Prática Jurídica Ética",
          "Revisão humana integral. Dever de veracidade (Art. 77, CPC). A responsabilidade técnica nunca é transferida à máquina.",
          "check")
    pilar(5, "Pilar 4 — Comunicação sobre o uso de IA",
          "Informar o cliente por escrito antes de usar a IA. Transparência não é opcional — é exigência regulatória.",
          "chat")

    # s6 CTA
    img, d, cx, cy, cw = new_slide(5, "REGULAÇÃO", 6)
    y = headline_box(d, cx, cy, cw, "Conformidade não é medo. É método.", 62, AMBER)
    y += 28
    y = body_box(d, cx, y, cw, "O checklist dos 4 pilares, com o que colocar em prática em cada um, está no site.", 34)
    footer(d, FW, FH, M, 6, T, "cta"); save(img, f"{base}/slide-6.png")

# ================================================================ STORIES 1080x1920
RW, RH, RM = 1080, 1920, 100

def story_frame(post_num, category, eyebrow, headline, fname, headline_color=PAPER,
                headline_size=92, sub=None, sticker=None, follow=None, cta=False):
    img = Image.new("RGB", (RW, RH), INK)
    watermark(img, 700, 1240, 760)
    d = ImageDraw.Draw(img)
    mt = 168
    d.text((RM, mt - 6), "§", font=font(SERIF, 34), fill=AMBER)
    tracked(d, (RM + 42, mt + 2), f"{post_num:02d} · {category}", font(MONO, 25), AMBER, tracking=7)
    d.line([(RM, mt + 46), (RW - RM, mt + 46)], fill=HAIR, width=2)
    y = mt + 92
    tracked(d, (RM, y), eyebrow, font(MONO, 27), AMBER, tracking=7)
    y += 76
    y = headline_box(d, RM, y, RW - 2 * RM, headline, headline_size, headline_color, leading=1.08)
    if sub:
        y += 26
        y = headline_box(d, RM, y, RW - 2 * RM, sub, 40, BODY_LT, leading=1.25, fnt=SERIF_I)
    if sticker:
        z0 = y + 70
        z1 = RH - 430
        if z1 > z0:
            d.rounded_rectangle([RM, z0, RW - RM, z1], radius=30, outline=HAIR, width=3)
            d.text((RW / 2, (z0 + z1) / 2), sticker, font=font(MONO, 30), fill=MUTED, anchor="mm")
    if follow:
        fy = RH - 372
        headline_box(d, RM, fy, RW - 2 * RM, follow, 40, PAPER, leading=1.26, fnt=GROT_B)
    # rodapé
    syl = RH - 196
    d.line([(RM, syl), (RW - RM, syl)], fill=HAIR, width=2)
    if cta:
        f = font(MONO_B, 30)
        tw = sum(d.textlength(c, font=f) + 5 for c in CTA) - 5
        pw, ph = tw + 88, 76
        x0 = (RW - pw) / 2
        rounded(d, [x0, syl + 48, x0 + pw, syl + 48 + ph], AMBER, radius=38)
        tracked(d, (x0 + 44, syl + 48 + ph / 2 - 16), CTA, f, INK, tracking=5)
    else:
        d.text((RM, syl + 40), "§", font=font(SERIF, 28), fill=AMBER)
        tracked(d, (RM + 34, syl + 46), BRAND, font(MONO, 22), MUTED, tracking=5)
    save(img, fname)

def stories():
    # POST 1
    story_frame(1, "GUIA", "ENQUETE · MANHÃ",
                "Para qual tarefa você mais usa IA hoje?",
                "post1-guia-ia/story-1-enquete.png",
                sticker="·  ENQUETE  ·  4 OPÇÕES  ·")
    story_frame(1, "GUIA", "A RESPOSTA",
                "Cada tarefa pede uma ferramenta diferente. Usar a errada custa a carteira.",
                "post1-guia-ia/story-2-resposta.png", headline_size=72, cta=True)
    story_frame(1, "GUIA", "DADO · NOITE",
                "11% → 30%.", "post1-guia-ia/story-3-dado.png",
                headline_color=AMBER, headline_size=150,
                sub="A adoção de IA em escritórios quase triplicou em 1 ano.")
    story_frame(1, "GUIA", "OS DOIS LADOS",
                "Os sem método são multados. Os com método ganham clientes. Em qual lado você está?",
                "post1-guia-ia/story-4-lados.png", headline_size=66, cta=True)

    # POST 2
    story_frame(2, "MÉTODO", "QUIZ · MANHÃ",
                "Qual parte do prompt evita a alucinação?",
                "post2-prompts/story-1-quiz.png",
                sticker="·  QUIZ  ·  3 OPÇÕES  ·")
    story_frame(2, "MÉTODO", "A RESPOSTA",
                "A restrição de fonte. Peça para usar EXCLUSIVAMENTE o texto que você colou.",
                "post2-prompts/story-2-resposta.png", headline_size=66, cta=True)
    story_frame(2, "MÉTODO", "NOITE",
                "Estrutura > criatividade.", "post2-prompts/story-3-estrutura.png",
                headline_size=84, sub="Os 3 prompts que mais economizam hora no escritório, testados.")
    story_frame(2, "MÉTODO", "O KIT",
                "Prontos para copiar, adaptar e usar com segurança.", "post2-prompts/story-4-kit.png",
                headline_size=66, cta=True)

    # POST 3
    story_frame(3, "PASSO A PASSO", "SEQUÊNCIA · MANHÃ",
                "7 passos. É o que separa uma petição eficiente de um processo disciplinar.",
                "post3-peticao-7-passos/story-1-sequencia.png",
                headline_size=72, sub="Qual passo você pula hoje?")
    story_frame(3, "PASSO A PASSO", "O CHECKLIST",
                "Os 7 passos completos estão no site.", "post3-peticao-7-passos/story-2-checklist.png",
                headline_size=74, cta=True)
    story_frame(3, "PASSO A PASSO", "AVISO · NOITE",
                "Passo 1 nunca é abrir o ChatGPT.", "post3-peticao-7-passos/story-3-aviso.png",
                headline_size=80, sub="É anonimizar. Colar processo com CPF do cliente é quebra de sigilo (Art. 34).")
    story_frame(3, "PASSO A PASSO", "O MÉTODO",
                "Anonimizar, pesquisar, travar, revisar, assinar.", "post3-peticao-7-passos/story-4-metodo.png",
                headline_size=66, cta=True)

    # POST 4 (caso real)
    story_frame(4, "CASO REAL", "CHOQUE · MANHÃ",
                "Número de processo. Relator. Ementa. Tudo falso.",
                "post4-caso-real/story-1-choque.png",
                headline_color=AMBER, headline_size=78,
                sub="Foi o que um advogado protocolou. A IA inventou — e a multa veio.")
    story_frame(4, "CASO REAL", "COMO EVITAR",
                "O protocolo que evita a multa está no site.", "post4-caso-real/story-2-evitar.png",
                headline_size=66, cta=True)
    story_frame(4, "CASO REAL", "RESPONSABILIDADE · NOITE",
                "Art. 77 do CPC: o dever de veracidade é seu.",
                "post4-caso-real/story-3-responsabilidade.png",
                headline_size=72, sub="Não do ChatGPT. Não do Claude. Seu.")
    story_frame(4, "CASO REAL", "A DEFESA",
                "Não peça para a IA citar. Você fornece a fonte.", "post4-caso-real/story-4-defesa.png",
                headline_size=66, cta=True)

    # POST 5
    story_frame(5, "REGULAÇÃO", "ENQUETE · MANHÃ",
                "Você já leu a Recomendação 001/2024 da OAB?",
                "post5-oab-4-pilares/story-1-enquete.png",
                sticker="·  ENQUETE  ·  3 OPÇÕES  ·")
    story_frame(5, "REGULAÇÃO", "OS 4 PILARES",
                "Cada pilar vira uma ação no seu escritório.", "post5-oab-4-pilares/story-2-pilares.png",
                headline_size=66, cta=True)
    story_frame(5, "REGULAÇÃO", "PILAR 4 · NOITE",
                "Avisar o cliente sobre IA. Por escrito. Antes de usar.",
                "post5-oab-4-pilares/story-3-pilar4.png",
                headline_size=66, sub="Esquecer isso é tão grave quanto colar o CPF no chat.")
    story_frame(5, "REGULAÇÃO", "O CHECKLIST",
                "O resumo executivo dos 4 pilares está no site.", "post5-oab-4-pilares/story-4-checklist.png",
                headline_size=66, cta=True)

# ================================================================ main
if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    print("POST 1 — GUIA");              p1()
    print("POST 2 — MÉTODO");            p2()
    print("POST 3 — PASSO A PASSO");     p3()
    print("POST 4 — CASO REAL (duotone)"); p4()
    print("POST 5 — REGULAÇÃO");         p5()
    print("STORIES");                    stories()
    print("\nConcluído →", OUT)
