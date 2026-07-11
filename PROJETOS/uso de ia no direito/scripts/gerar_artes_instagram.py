#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as artes do plano de publicação Instagram — sistema 'Dossiê'.

Anatomia de cada peça: etiqueta de classificação (mono) no alto · tese
(grotesca bold) · evidência em painel claro · despacho/CTA no pé · marca
d'água § · fio do protocolo (tracejado→sólido).
"""

import os
from PIL import Image, ImageDraw, ImageFont

ROOT = "/media/mascarenhas/01D7475AEEEB8480/segundo-cerebro/Segundo-Cerebro/PROJETOS/uso de ia no direito"
FONTS = os.path.join(ROOT, ".claude/skills/canvas-design/canvas-fonts")

# ---------------------------------------------------------------- tokens
INK = "#191d30"      # fundo / autoridade
PAPER = "#f4f3ee"    # texto sobre escuro
ORANGE = "#f16520"   # gesto de ação
RED = "#fbecea"      # casos reais / erros
BLUE = "#eef1fb"     # blocos legais
GREEN = "#ecf6f0"    # condutas corretas
MUTED = "#9aa0b8"    # texto secundário sobre escuro
HAIR = "#31374f"     # filetes sobre escuro
WM = "#1e2338"       # marca d'água §
DARK_MUTED = "#5a5f75"  # texto secundário sobre painéis claros

CTA = "CONHEÇA O SITE — LINK NA BIO"
BRAND = "IA NA ADVOCACIA"

F = {}
# Work Sans e Bricolage Grotesque vêm como fontes variáveis: mapeia o nome
# lógico (peso) para o arquivo VF + instância nomeada.
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
GROT_R = "BricolageGrotesque-Regular.ttf"
MONO = "IBMPlexMono-Regular.ttf"
MONO_B = "IBMPlexMono-Bold.ttf"
SERIF_I = "IBMPlexSerif-Italic.ttf"
SERIF = "IBMPlexSerif-Regular.ttf"
SANS = "WorkSans-Regular.ttf"
SANS_B = "WorkSans-Bold.ttf"

# ---------------------------------------------------------------- helpers
def wrap(d, text, fnt, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def tracked(d, xy, text, fnt, fill, tracking=5, anchor_right=None, canvas_w=None):
    """Texto com letter-spacing manual. Se anchor_right, alinha à direita."""
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

def protocol_line(d, x0, y, x1, color):
    """O fio do protocolo: tracejado na 1ª metade, sólido na 2ª."""
    mid = x0 + (x1 - x0) * 0.45
    dashed_line(d, x0, y, mid, color)
    d.line([(mid, y), (x1, y)], fill=color, width=2)
    d.ellipse([x1 - 5, y - 4, x1 + 3, y + 4], fill=color)

def icon(d, kind, cx, cy, r, col_fg, col_ring):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col_ring, width=3)
    s = r * 0.45
    if kind == "check":
        d.line([(cx - s, cy), (cx - s * 0.2, cy + s * 0.8)], fill=col_fg, width=5)
        d.line([(cx - s * 0.2, cy + s * 0.8), (cx + s, cy - s * 0.7)], fill=col_fg, width=5)
    elif kind == "cross":
        d.line([(cx - s, cy - s), (cx + s, cy + s)], fill=col_fg, width=5)
        d.line([(cx - s, cy + s), (cx + s, cy - s)], fill=col_fg, width=5)
    elif kind == "warn":
        d.line([(cx, cy - s), (cx, cy + s * 0.35)], fill=col_fg, width=5)
        d.ellipse([cx - 3, cy + s * 0.7 - 3, cx + 3, cy + s * 0.7 + 3], fill=col_fg)

def num_badge(d, n, cx, cy, r, fg, bg):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=bg)
    f = font(MONO_B, int(r * 1.1))
    d.text((cx, cy - 2), str(n), font=f, fill=fg, anchor="mm")

def watermark(img, x, y, size=760):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    dl = ImageDraw.Draw(layer)
    dl.text((x, y), "§", font=font("Gloock-Regular.ttf", size), fill=WM)
    img.paste(Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB"), (0, 0))

def arrow(d, x, y, ln, color, w=3):
    d.line([(x, y), (x + ln, y)], fill=color, width=w)
    d.line([(x + ln - 14, y - 10), (x + ln, y)], fill=color, width=w)
    d.line([(x + ln - 14, y + 10), (x + ln, y)], fill=color, width=w)
    return ln

def rounded(d, box, fill, radius=26, outline=None, width=2):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

# ---------------------------------------------------------------- chrome
def header(img, d, W, M, eyebrow, page=None, total=None, accent=ORANGE):
    # marca + etiqueta de série
    d.text((M, M), "§", font=font(SERIF, 40), fill=accent)
    tracked(d, (M + 56, M + 8), BRAND, font(MONO, 26), MUTED, tracking=6)
    if page:
        tracked(d, (M, M + 8), f"{page:02d}/{total:02d}", font(MONO, 26), MUTED,
                tracking=4, anchor_right=True, canvas_w=W)
    y = M + 78
    protocol_line(d, M, y, W - M, HAIR)
    ey = y + 34
    tracked(d, (M, ey), eyebrow, font(MONO, 27), accent, tracking=7)
    return ey + 78

def footer(img, d, W, H, M, mode="cta", accent=ORANGE, swipe_label="ARRASTE"):
    yline = H - 168
    d.line([(M, yline), (W - M, yline)], fill=HAIR, width=2)
    cy = yline + 84
    if mode == "cta":
        f = font(MONO_B, 30)
        tw = sum(d.textlength(c, font=f) + 6 for c in CTA) - 6
        pw, ph = tw + 96, 92
        x0 = (W - pw) / 2
        rounded(d, [x0, cy - ph / 2, x0 + pw, cy + ph / 2], accent, radius=46)
        tracked(d, (x0 + 48, cy - 17), CTA, f, INK, tracking=6)
    elif mode == "swipe":
        tracked(d, (M, cy - 15), BRAND + " · OAB & LGPD", font(MONO, 25), MUTED, tracking=5)
        f = font(MONO_B, 27)
        lab = swipe_label
        tw = sum(d.textlength(c, font=f) + 5 for c in lab) - 5
        ax = W - M - 64
        tracked(d, (W - M - 64 - tw - 18, cy - 14), lab, f, PAPER, tracking=5)
        arrow(d, ax, cy, 60, accent)
    elif mode == "brand":
        tracked(d, (M, cy - 15), BRAND + " · OAB & LGPD", font(MONO, 25), MUTED, tracking=5)

def headline(d, W, M, y, text, size, color=PAPER, maxw=None, leading=1.12, fnt=GROT_B):
    f = font(fnt, size)
    for ln in wrap(d, text, f, maxw or (W - 2 * M)):
        d.text((M, y), ln, font=f, fill=color)
        y += int(size * leading)
    return y

def body(d, W, M, y, text, size=38, color=MUTED, maxw=None, leading=1.42, fnt=SANS):
    f = font(fnt, size)
    for ln in wrap(d, text, f, maxw or (W - 2 * M)):
        d.text((M, y), ln, font=f, fill=color)
        y += int(size * leading)
    return y

def panel_list(d, W, M, y, items, tint, kind=None, numbered=False, item_size=37,
               title=None, mono_items=False, H_cap=None):
    pad = 52
    f = font(MONO if mono_items else SANS, item_size)
    fb = font(SANS_B, item_size)
    inner_w = W - 2 * M - 2 * pad - (74 if (kind or numbered) else 0)
    # mede altura
    rows = []
    for it in items:
        t = it if isinstance(it, str) else it[0]
        lines = wrap(d, t, fb if (isinstance(it, tuple) and it[1]) else f, inner_w)
        rows.append((it, lines))
    lh = int(item_size * 1.32)
    gap = 34
    htitle = 64 if title else 0
    ph = pad * 2 + htitle + sum(len(l) * lh for _, l in rows) + gap * (len(rows) - 1)
    rounded(d, [M, y, W - M, y + ph], tint, radius=30)
    cy = y + pad
    if title:
        tracked(d, (M + pad, cy), title, font(MONO_B, 28), INK, tracking=6)
        cy += htitle
    for it, lines in rows:
        bold = isinstance(it, tuple) and it[1]
        x0 = M + pad
        if kind:
            icon(d, kind, x0 + 22, cy + lh // 2 - 2, 22,
                 ORANGE if kind == "warn" else INK, DARK_MUTED)
            x0 += 74
        if numbered:
            num_badge(d, rows.index((it, lines)) + 1, x0 + 22, cy + lh // 2 - 2, 23, PAPER, INK)
            x0 += 74
        for ln in lines:
            d.text((x0, cy), ln, font=fb if bold else f, fill=INK)
            cy += lh
        cy += gap
    return y + ph

def kv_rows(d, W, M, y, rows, accent=ORANGE, size=33):
    """Linhas tipo registro: filete + texto mono."""
    f = font(MONO, size)
    for r in rows:
        d.line([(M, y), (M + 34, y)], fill=accent, width=4)
        x = M + 56
        for ln in wrap(d, r, f, W - M - x):
            d.text((x, y - size // 2 - 4), ln, font=f, fill=PAPER)
            y += int(size * 1.45)
        y += 26
    return y

def quote_block(d, W, M, y, text, size=54, color=PAPER, maxw=None):
    d.text((M, y - 30), "“", font=font(SERIF_I, int(size * 2.4)), fill=ORANGE)
    y += int(size * 1.1)
    f = font(SERIF_I, size)
    for ln in wrap(d, text, f, maxw or (W - 2 * M - 40)):
        d.text((M + 40, y), ln, font=f, fill=color)
        y += int(size * 1.3)
    return y

# ---------------------------------------------------------------- canvas
def canvas(W, H):
    img = Image.new("RGB", (W, H), INK)
    return img, ImageDraw.Draw(img)

def save(img, rel):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, "PNG")
    print("ok", rel)

# ================================================================ FEED 1080x1350
FW, FH, FM = 1080, 1350, 84

def feed_base(eyebrow, page=None, total=None, accent=ORANGE, wm_xy=(700, 760)):
    img, d = canvas(FW, FH)
    watermark(img, *wm_xy)
    d = ImageDraw.Draw(img)
    y = header(img, d, FW, FM, eyebrow, page, total, accent)
    return img, d, y

# ---- A1
def a1():
    img, d, y = feed_base("CASOS REAIS · 2025–2026", accent=ORANGE)
    y = headline(d, FW, FM, y + 8, "3 advogados multados por confiar na IA.", 92)
    y = body(d, FW, FM, y + 26, "Nenhum agiu de má-fé. Faltou protocolo.", 42, PAPER)
    y += 44
    y = panel_list(d, FW, FM, y, [
        "Justiça Federal · PR — 20 salários-mínimos",
        "TRT-2 · SP — 5% sobre o valor da causa",
        "TJSC · SC — 10% + comunicação à OAB",
    ], RED, mono_items=True, item_size=34)
    footer(img, d, FW, FH, FM, "cta")
    save(img, "instagram-imagens/post1-feed.png")

# ---- A1 versão story (1080x1920) — definida após o bloco REELS/STORY

# ---- A2 carrossel 8
def a2():
    base = "instagram-imagens/post2-carrossel-3erros"
    T = 8
    # s1 capa
    img, d, y = feed_base("OS 3 ERROS · IA NA ADVOCACIA", 1, T)
    y = headline(d, FW, FM, y + 10, "77% dos advogados já usam IA.", 96)
    y = body(d, FW, FM, y + 30, "E a maioria comete um destes 3 erros — sem saber.", 44, PAPER)
    footer(img, d, FW, FH, FM, "swipe")
    save(img, f"{base}/slide-1.png")
    # pares erro/correção
    def erro(n, page, tese, corpo):
        img, d, y = feed_base(f"ERRO {n} DE 3", page, T, accent=ORANGE)
        y = headline(d, FW, FM, y + 8, tese, 78)
        y += 36
        pad = 52
        f = font(SANS, 40)
        lines = wrap(d, corpo, f, FW - 2 * FM - 2 * pad - 74)
        ph = pad * 2 + len(lines) * int(40 * 1.4)
        rounded(d, [FM, y, FW - FM, y + ph], RED, radius=30)
        icon(d, "cross", FM + pad + 22, y + pad + 22, 22, INK, DARK_MUTED)
        cy = y + pad
        for ln in lines:
            d.text((FM + pad + 74, cy), ln, font=f, fill=INK)
            cy += int(40 * 1.4)
        footer(img, d, FW, FH, FM, "swipe")
        save(img, f"{base}/slide-{page}.png")
    def fix(n, page, tese, items, mono=False):
        img, d, y = feed_base(f"CORREÇÃO {n}", page, T, accent=ORANGE)
        y = headline(d, FW, FM, y + 8, tese, 78)
        y += 36
        y = panel_list(d, FW, FM, y, items, GREEN, kind="check",
                       item_size=34 if mono else 38, mono_items=mono)
        footer(img, d, FW, FH, FM, "swipe")
        save(img, f"{base}/slide-{page}.png")
    erro(1, 2, "Dados de cliente no ChatGPT grátis.",
         "Nas versões públicas, suas conversas podem treinar o modelo. Sigilo profissional (Art. 34) e LGPD em risco.")
    fix(1, 3, "Anonimize antes do prompt.", [
        "João da Silva  →  [CLIENTE]",
        "123.456.789-00  →  [CPF]",
        "R$ 450.000,00  →  [VALOR]",
        "0801234-55.2025  →  [Nº PROC]",
    ], mono=True)
    erro(2, 4, "Pedir jurisprudência sem dar a fonte.",
         "A IA não consulta tribunais. Ela prevê o texto mais provável — e inventa precedentes convincentes.")
    fix(2, 5, "Você fornece a decisão. A IA estrutura.", [
        "Pesquise na fonte oficial",
        "Cole a decisão real no prompt",
        "Instrua: “use somente esta decisão”",
    ])
    erro(3, 6, "Usar IA sem informar o cliente.",
         "A Recomendação 001/2024 (item 4) exige formalização por escrito — e o cliente pode recusar.")
    fix(3, 7, "Cláusula de IA no contrato.", [
        "Uma cláusula no contrato de honorários",
        "Todo cliente novo já entra coberto",
        "Assinou, está documentado",
    ])
    # s8 CTA
    img, d, y = feed_base("O KIT RESOLVE OS 3", 8, T)
    y = headline(d, FW, FM, y + 10, "Cláusula, prompts e tabela de anonimização — prontos.", 80)
    y = body(d, FW, FM, y + 30, "Implementação no mesmo dia, com base na Recomendação 001/2024.", 42)
    footer(img, d, FW, FH, FM, "cta")
    save(img, f"{base}/slide-8.png")

# ---- A3 carrossel 6
def a3():
    base = "instagram-imagens/post3-carrossel-oab"
    T = 6
    img, d, y = feed_base("RECOMENDAÇÃO 001/2024 · OAB", 1, T)
    y = headline(d, FW, FM, y + 10, "O que pode e o que é vedado com IA.", 94)
    y = body(d, FW, FM, y + 30, "O mapa de referência para o uso seguro na advocacia.", 44, PAPER)
    footer(img, d, FW, FH, FM, "swipe")
    save(img, f"{base}/slide-1.png")
    def zona(page, tag, tint, kind, tese, items):
        img, d, y = feed_base(tag, page, T)
        y = headline(d, FW, FM, y + 8, tese, 76)
        y += 36
        y = panel_list(d, FW, FM, y, items, tint, kind=kind, item_size=36)
        footer(img, d, FW, FH, FM, "swipe")
        save(img, f"{base}/slide-{page}.png")
    zona(2, "ZONA 1 · PODE", GREEN, "check", "Uso livre, com bom senso.", [
        "Resumir documentos e processos",
        "Organizar jurisprudência que você pesquisou",
        "Estruturar argumentos com as suas fontes",
        "Roteiros de audiência e checklists",
    ])
    zona(3, "ZONA 2 · COM MÉTODO", BLUE, "warn", "A área cinzenta — onde a maioria escorrega.", [
        "Redigir peças — rascunho + revisão integral",
        "Revisar contratos — anonimização + DPA",
        "Chatbot — informa e agenda, não orienta",
        "Marketing — dentro do Provimento 205/2021",
    ])
    zona(4, "ZONA 3 · VEDADO", RED, "cross", "Infração disciplinar, com ou sem intenção.", [
        "Jurisprudência sem verificar na fonte",
        "Protocolar sem revisão integral",
        "Parecer direto ao cliente via IA",
        "Dados reais em IA pública sem DPA",
    ])
    # s5 regra síntese
    img, d, y = feed_base("A REGRA QUE ORGANIZA TUDO", 5, T)
    y = quote_block(d, FW, FM, y + 60, "A IA acelera o processo. O advogado responde pelo resultado.", 62)
    footer(img, d, FW, FH, FM, "swipe")
    save(img, f"{base}/slide-5.png")
    img, d, y = feed_base("REFERÊNCIA COMPLETA", 6, T)
    y = headline(d, FW, FM, y + 10, "A tabela completa, com a base legal de cada item.", 82)
    y = body(d, FW, FM, y + 30, "Pronta para imprimir e mandar para a equipe.", 42)
    footer(img, d, FW, FH, FM, "cta")
    save(img, f"{base}/slide-6.png")

# ================================================================ REELS / STORY 1080x1920
RW, RH, RM = 1080, 1920, 96

def reel_base(eyebrow, page=None, total=None, accent=ORANGE):
    img, d = canvas(RW, RH)
    watermark(img, 660, 1280, 820)
    d = ImageDraw.Draw(img)
    # safe area: começa mais baixo
    d.text((RM, 200), "§", font=font(SERIF, 44), fill=accent)
    tracked(d, (RM + 60, 210), BRAND, font(MONO, 28), MUTED, tracking=6)
    if page:
        tracked(d, (RM, 210), f"{page:02d}/{total:02d}", font(MONO, 28), MUTED,
                tracking=4, anchor_right=True, canvas_w=RW)
    yl = 286
    protocol_line(d, RM, yl, RW - RM, HAIR)
    tracked(d, (RM, yl + 40), eyebrow, font(MONO, 29), accent, tracking=7)
    return img, d, yl + 130

def reel_footer(img, d, mode="brand"):
    yline = RH - 300
    d.line([(RM, yline), (RW - RM, yline)], fill=HAIR, width=2)
    cy = yline + 96
    if mode == "cta":
        f = font(MONO_B, 32)
        tw = sum(d.textlength(c, font=f) + 6 for c in CTA) - 6
        pw, ph = tw + 100, 100
        x0 = (RW - pw) / 2
        rounded(d, [x0, cy - ph / 2, x0 + pw, cy + ph / 2], ORANGE, radius=50)
        tracked(d, (x0 + 50, cy - 18), CTA, f, INK, tracking=6)
    else:
        tracked(d, (RM, cy - 16), BRAND + " · OAB & LGPD", font(MONO, 27), MUTED, tracking=5)

def reel_headline(d, y, text, size=104, color=PAPER):
    return headline(d, RW, RM, y, text, size, color)

def a4():
    base = "instagram-imagens/post4-reels-estagiario"
    T = 6
    img, d, y = reel_base("CASO REAL · TRT-2 · 2026", 1, T)
    y = reel_headline(d, y + 30, "“A IA gerou” não é defesa.", 116)
    y = body(d, RW, RM, y + 40, "“Foi o estagiário” também não.", 54, PAPER)
    reel_footer(img, d); save(img, f"{base}/cena-1.png")

    img, d, y = reel_base("O CASO", 2, T)
    y = reel_headline(d, y + 30, "Precedentes inventados por IA num recurso.", 100)
    y = kv_rows(d, RW, RM, y + 70, ["TRT-2 · São Paulo/SP", "16/02/2026", "Fonte: ConJur"], size=36)
    reel_footer(img, d); save(img, f"{base}/cena-2.png")

    img, d, y = reel_base("A SANÇÃO", 3, T)
    d.text((RM, y + 60), "5%", font=font(GROT_B, 360), fill=ORANGE)
    y = body(d, RW, RM, y + 480, "de multa sobre o valor da causa, por litigância de má-fé — e ofício à OAB-SP.", 52, PAPER)
    reel_footer(img, d); save(img, f"{base}/cena-3.png")

    img, d, y = reel_base("A DEFESA", 4, T)
    y = quote_block(d, RW, RM, y + 60, "Foi o estagiário que preparou a peça.", 72)
    reel_footer(img, d); save(img, f"{base}/cena-4.png")

    img, d, y = reel_base("O TRIBUNAL", 5, T)
    y = quote_block(d, RW, RM, y + 60, "O dever de supervisão é indelegável.", 72)
    y = kv_rows(d, RW, RM, y + 80, ["Recomendação 001/2024 · item 3.6", "Art. 77 · CPC"], size=36)
    reel_footer(img, d); save(img, f"{base}/cena-5.png")

    img, d, y = reel_base("A SOLUÇÃO", 6, T)
    y = reel_headline(d, y + 30, "Política interna de IA pronta para adaptar.", 100)
    y = body(d, RW, RM, y + 40, "Ferramentas aprovadas, revisão obrigatória, registro de uso.", 50)
    reel_footer(img, d, "cta"); save(img, f"{base}/cena-6.png")

def a5():
    base = "instagram-imagens/post5-reels-prompt"
    T = 6
    img, d, y = reel_base("O PROTOCOLO ANTI-ALUCINAÇÃO", 1, T)
    y = reel_headline(d, y + 30, "1 parágrafo elimina a jurisprudência falsa.", 112)
    reel_footer(img, d); save(img, f"{base}/cena-1.png")

    img, d, y = reel_base("POR QUÊ", 2, T)
    y = reel_headline(d, y + 30, "A IA não consulta tribunais.", 104)
    y = body(d, RW, RM, y + 40, "Ela prevê o texto mais provável — e inventa citações convincentes.", 52, PAPER)
    reel_footer(img, d); save(img, f"{base}/cena-2.png")

    img, d, y = reel_base("O PROMPT", 3, T)
    pad = 56
    txt = ("Use exclusivamente as fontes que eu colar abaixo. Não cite nenhuma lei, "
           "súmula ou decisão que não esteja no texto fornecido. Se faltar informação, "
           "pergunte — não invente.")
    f = font(MONO, 40)
    lines = wrap(d, txt, f, RW - 2 * RM - 2 * pad)
    ph = pad * 2 + len(lines) * int(40 * 1.5)
    y += 40
    rounded(d, [RM, y, RW - RM, y + ph], BLUE, radius=30)
    cy = y + pad
    for ln in lines:
        d.text((RM + pad, cy), ln, font=f, fill=INK)
        cy += int(40 * 1.5)
    y = body(d, RW, RM, y + ph + 50, "Copie. Cole no início de toda tarefa jurídica.", 48, PAPER)
    reel_footer(img, d); save(img, f"{base}/cena-3.png")

    img, d, y = reel_base("A LÓGICA", 4, T)
    y = reel_headline(d, y + 30, "Você fornece a fonte. A IA estrutura.", 104)
    y = body(d, RW, RM, y + 40, "Descoberta é onde ela alucina. Estrutura é onde ela rende.", 52, PAPER)
    reel_footer(img, d); save(img, f"{base}/cena-4.png")

    img, d, y = reel_base("MESMO ASSIM", 5, T)
    y = reel_headline(d, y + 30, "Confira tudo no tribunal antes de protocolar.", 100)
    y = kv_rows(d, RW, RM, y + 70, ["Art. 77 · CPC — dever de veracidade", "Recomendação 001/2024 · item 3.7"], size=36)
    reel_footer(img, d); save(img, f"{base}/cena-5.png")

    img, d, y = reel_base("O KIT", 6, T)
    y = reel_headline(d, y + 30, "Este é 1 de 7 prompts com segurança embutida.", 100)
    y = body(d, RW, RM, y + 40, "Junto: cláusula de IA para o contrato e tabela de anonimização.", 50)
    reel_footer(img, d, "cta"); save(img, f"{base}/cena-6.png")

def a6():
    base = "instagram-imagens/post6-story"
    def story(n, eyebrow, tese, hint, cta=False):
        img, d, y = reel_base(eyebrow)
        y = reel_headline(d, y + 40, tese, 100)
        if hint:
            # zona reservada para a figurinha nativa
            zy0, zy1 = y + 120, RH - 480
            d.rounded_rectangle([RM, zy0, RW - RM, zy1], radius=34, outline=HAIR, width=3)
            f = font(MONO, 30)
            d.text((RW / 2, (zy0 + zy1) / 2), hint, font=f, fill=MUTED, anchor="mm")
        reel_footer(img, d, "cta" if cta else "brand")
        save(img, f"{base}/story-{n}.png")
    story(1, "ENQUETE", "Você já confiou numa resposta da IA sem checar?", "· figurinha de enquete aqui ·")
    story(2, "CAIXINHA", "Qual tarefa mais consome o seu tempo no escritório?", "· caixinha de perguntas aqui ·")
    story(3, "CAIXINHA", "O que você queria saber sobre IA × OAB?", "· caixinha de perguntas aqui ·")
    story(4, "O MÉTODO", "Prompts, cláusula e checklist — prontos no site.", None, cta=True)

# ---- A1 story: mesma mensagem do post1-feed, em 1080x1920
def a1_story():
    img, d, y = reel_base("CASOS REAIS · 2025–2026", accent=ORANGE)
    y = reel_headline(d, y + 30, "3 advogados multados por confiar na IA.", 108)
    y = body(d, RW, RM, y + 40, "Nenhum agiu de má-fé. Faltou protocolo.", 50, PAPER)
    y += 56
    y = panel_list(d, RW, RM, y, [
        "Justiça Federal · PR — 20 salários-mínimos",
        "TRT-2 · SP — 5% sobre o valor da causa",
        "TJSC · SC — 10% + comunicação à OAB",
    ], RED, mono_items=True, item_size=36)
    reel_footer(img, d, "cta")
    save(img, "instagram-imagens/post1-story.png")

# ---- A2 story: resumo do carrossel "3 erros" em 1080x1920
def a2_story():
    img, d, y = reel_base("OS 3 ERROS · IA NA ADVOCACIA", accent=ORANGE)
    y = reel_headline(d, y + 30, "77% já usam IA. E cometem 3 erros.", 104)
    y = body(d, RW, RM, y + 40, "Quase ninguém percebe que comete.", 50, PAPER)
    y += 56
    y = panel_list(d, RW, RM, y, [
        "Dados de cliente no ChatGPT grátis",
        "Jurisprudência sem fornecer a fonte",
        "Usar IA sem informar o cliente",
    ], RED, kind="cross", item_size=37)
    reel_footer(img, d, "cta")
    save(img, "instagram-imagens/post2-story.png")

# ---- A3 story: resumo do carrossel "pode / vedado" em 1080x1920
def a3_story():
    img, d, y = reel_base("RECOMENDAÇÃO 001/2024 · OAB", accent=ORANGE)
    y = reel_headline(d, y + 30, "Pode ou é vedado?", 128)
    y += 64
    y = panel_list(d, RW, RM, y, ["Resumir e organizar suas fontes"],
                   GREEN, kind="check", title="PODE", item_size=36)
    y += 24
    y = panel_list(d, RW, RM, y, ["Redigir e revisar — com método"],
                   BLUE, kind="warn", title="COM MÉTODO", item_size=36)
    y += 24
    y = panel_list(d, RW, RM, y, ["Jurisprudência sem checar a fonte"],
                   RED, kind="cross", title="VEDADO", item_size=36)
    reel_footer(img, d, "cta")
    save(img, "instagram-imagens/post3-story.png")

# ================================================================ SÉRIE B (multas)
def serie_b():
    base = "instagram-serie-multas"
    img, d, y = feed_base("SÉRIE · MULTADOS POR IA")
    y = headline(d, FW, FM, y + 10, "4 advogados. 4 estados. O mesmo erro.", 92)
    y = body(d, FW, FM, y + 28, "Casos reais, com fonte. Um por post.", 42, PAPER)
    y += 46
    y = kv_rows(d, FW, FM, y, ["Justiça Federal · PR", "TRT-2 · SP", "TRT-3 · MG", "TJSC · SC"])
    footer(img, d, FW, FH, FM, "swipe", swipe_label="ACOMPANHE")
    save(img, f"{base}/post-1-capa.png")

    def caso(slug, n, court, tese, rows, fonte):
        img, d, y = feed_base(f"CASO {n}/4 · {court}")
        y = headline(d, FW, FM, y + 8, tese, 84)
        y += 40
        y = panel_list(d, FW, FM, y, rows, RED, mono_items=True, item_size=33)
        tracked(d, (FM, y + 36), fonte, font(MONO, 26), MUTED, tracking=4)
        footer(img, d, FW, FH, FM, "cta")
        save(img, f"{base}/{slug}.png")
    caso("post-2-jf-pr", 1, "JUSTIÇA FEDERAL · LONDRINA/PR · 02/07/2025",
         "Artigos de lei que não existem.",
         ["Multa: 20 salários-mínimos",
          "Litigância de má-fé + ato atentatório",
          "Ofício à OAB-PR"],
         "FONTE: MIGALHAS · 02/07/2025")
    caso("post-3-trt2-sp", 2, "TRT-2 · SÃO PAULO/SP · 16/02/2026",
         "Precedentes falsos. Culpou o estagiário.",
         ["Multa: 5% sobre o valor da causa",
          "“O dever de supervisão é indelegável”",
          "Ofício à OAB-SP"],
         "FONTE: CONJUR · 16/02/2026")
    caso("post-4-trt3-mg", 3, "TRT-3 · ARAÇUAÍ/MG · 27/10/2025",
         "A súmula que nunca existiu.",
         ["Multa: R$ 1.200 por má-fé",
          "“Faltou boa-fé processual”",
          "A tese caiu junto com a súmula"],
         "FONTE: TRT-3 · 27/10/2025")
    caso("post-5-tjsc", 4, "TJSC · SANTA CATARINA · 18/02/2025",
         "Admitiu o ChatGPT. Não adiantou.",
         ["Multa: 10% do valor da causa",
          "Dever de veracidade — Art. 77 CPC",
          "Comunicação à OAB/SC"],
         "FONTE: JUSBRASIL · 18/02/2025")

    img, d, y = feed_base("A LIÇÃO DA SÉRIE")
    y = headline(d, FW, FM, y + 8, "Ninguém verificou na fonte.", 88)
    y += 40
    y = panel_list(d, FW, FM, y, [
        "Fonte primeiro — você pesquisa",
        "Prompt com trava — “não invente”",
        "Revisão integral antes do protocolo",
        "Registro — ferramenta, tarefa, revisor",
    ], GREEN, numbered=True, item_size=36)
    footer(img, d, FW, FH, FM, "cta")
    save(img, f"{base}/post-6-licao.png")

# ================================================================ SÉRIE C (positiva)
def serie_c():
    base = "instagram-serie-oab-positivo"
    img, d, y = feed_base("SÉRIE · O OUTRO LADO")
    y = quote_block(d, FW, FM, y + 30, "A OAB é contra a IA.", 76)
    y = headline(d, FW, FM, y + 50, "Será?", 120, ORANGE)
    y = body(d, FW, FM, y + 40, "O que a Ordem e o Judiciário realmente fazem — com fonte.", 42, PAPER)
    footer(img, d, FW, FH, FM, "swipe", swipe_label="ACOMPANHE")
    save(img, f"{base}/post-1-capa.png")

    # C2 STF
    img, d, y = feed_base("STF · PROJETO VICTOR · DESDE 2018")
    y = headline(d, FW, FM, y + 8, "O Supremo usa IA desde antes do ChatGPT.", 80)
    y += 60
    f = font(GROT_B, 110)
    d.text((FM, y), "150 mil", font=f, fill=MUTED)
    aw = d.textlength("150 mil", font=f)
    arrow(d, FM + aw + 36, y + 78, 90, ORANGE, w=6)
    d.text((FM + aw + 162, y), "20 mil", font=f, fill=PAPER)
    y = body(d, FW, FM, y + 170, "processos no acervo — redução com apoio de IA.", 42)
    tracked(d, (FM, y + 26), "FONTE: CONJUR · 2026", font(MONO, 26), MUTED, tracking=4)
    footer(img, d, FW, FH, FM, "cta")
    save(img, f"{base}/post-2-stf-victor.png")

    # C3 STJ
    img, d, y = feed_base("STJ · PROJETO ATHOS")
    y = headline(d, FW, FM, y + 8, "A IA que uniformiza a jurisprudência.", 84)
    y += 40
    y = panel_list(d, FW, FM, y, [
        "Classifica recursos especiais",
        "Agrupa precedentes por tese",
        "Supervisão humana em cada etapa",
    ], GREEN, kind="check", item_size=38)
    footer(img, d, FW, FH, FM, "cta")
    save(img, f"{base}/post-3-stj-athos.png")

    # C4 13 tribunais
    img, d, y = feed_base("CNJ · RESOLUÇÃO 615/2025")
    d.text((FM, y + 10), "13", font=font(GROT_B, 300), fill=ORANGE)
    y = headline(d, FW, FM, y + 330, "tribunais já usam IA na admissibilidade de recursos.", 72)
    y += 36
    y = kv_rows(d, FW, FM, y, [
        "CNIAJ 1/2026 — rastreio de manipulação nos autos",
        "PROSEG-IA — segurança permanente",
    ])
    footer(img, d, FW, FH, FM, "cta")
    save(img, f"{base}/post-4-13-tribunais.png")

    # C5 cursos
    img, d, y = feed_base("OAB-SP & OAB-PR")
    y = headline(d, FW, FM, y + 8, "A própria OAB ensina IA. De graça.", 86)
    y += 40
    y = panel_list(d, FW, FM, y, [
        "Curso gratuito de IA generativa",
        "Com Trybe, Jusbrasil e ITS Rio",
        "Item 3.5 — aprendizagem contínua",
    ], BLUE, kind="check", item_size=38)
    footer(img, d, FW, FH, FM, "cta")
    save(img, f"{base}/post-5-oab-cursos.png")

    # C6 LIAD
    img, d, y = feed_base("OAB-CE · LIAD · 2026")
    y = headline(d, FW, FM, y + 8, "Um laboratório de IA dentro da OAB.", 84)
    y += 60
    f = font(GROT_B, 110)
    d.text((FM, y), "37%", font=f, fill=MUTED)
    aw = d.textlength("37%", font=f)
    arrow(d, FM + aw + 36, y + 78, 90, ORANGE, w=6)
    d.text((FM + aw + 162, y), "80%", font=f, fill=PAPER)
    y = body(d, FW, FM, y + 170, "adoção de IA em escritórios — 2024 → 2025.", 42)
    tracked(d, (FM, y + 26), "FONTES: O VEREDITO · NETDOCUMENTS", font(MONO, 26), MUTED, tracking=4)
    footer(img, d, FW, FH, FM, "cta")
    save(img, f"{base}/post-6-oab-ce-liad.png")

    # C7 fechamento
    img, d, y = feed_base("O FECHO DA SÉRIE")
    y = headline(d, FW, FM, y + 8, "A IA é incentivada. Usar errado é que dá multa.", 78)
    y += 36
    y = panel_list(d, FW, FM, y, [
        "Dados protegidos — anonimização + DPA",
        "Fonte sempre humana — Art. 77 CPC",
        "Revisão integral — item 3.7",
        "Cliente informado — item 4",
    ], GREEN, numbered=True, item_size=35)
    footer(img, d, FW, FH, FM, "cta")
    save(img, f"{base}/post-7-fechamento.png")

# ================================================================ SÉRIE D (LGPD) x2 versões
def serie_d(folder, mono):
    """mono=True → versão monocromática: painéis viram caixas contornadas."""
    T = 8
    tintB = INK if mono else BLUE
    tintR = INK if mono else RED
    tintG = INK if mono else GREEN
    def panel(d, y, items, tint, **kw):
        if mono:
            # painel contornado: desenha manualmente
            pad = 52
            f = font(SANS, kw.get("item_size", 37))
            inner_w = FW - 2 * FM - 2 * pad - (74 if kw.get("kind") or kw.get("numbered") else 0)
            rows = [(it, wrap(d, it if isinstance(it, str) else it[0], f, inner_w)) for it in items]
            lh = int(kw.get("item_size", 37) * 1.32)
            gap = 34
            ph = pad * 2 + sum(len(l) * lh for _, l in rows) + gap * (len(rows) - 1)
            rounded(d, [FM, y, FW - FM, y + ph], None, radius=30, outline=HAIR, width=3)
            cy = y + pad
            for i, (it, lines) in enumerate(rows):
                x0 = FM + pad
                if kw.get("kind"):
                    icon(d, kw["kind"], x0 + 22, cy + lh // 2 - 2, 22, ORANGE, HAIR)
                    x0 += 74
                if kw.get("numbered"):
                    num_badge(d, i + 1, x0 + 22, cy + lh // 2 - 2, 23, INK, ORANGE)
                    x0 += 74
                for ln in lines:
                    d.text((x0, cy), ln, font=f, fill=PAPER)
                    cy += lh
                cy += gap
            return y + ph
        return panel_list(d, FW, FM, y, items, tint, **kw)

    def slide(n, eyebrow, build):
        img, d, y = feed_base(eyebrow, n, T)
        build(img, d, y)
        save(img, f"{folder}/slide-{n}.png")

    def s1(img, d, y):
        y = headline(d, FW, FM, y + 10, "Onde você cola os dados do cliente?", 92)
        y = body(d, FW, FM, y + 30, "O risco invisível das IAs gratuitas — e o protocolo que o elimina.", 44, PAPER)
        footer(img, d, FW, FH, FM, "swipe")
    def s2(img, d, y):
        y = headline(d, FW, FM, y + 8, "Versões públicas podem treinar com as suas conversas.", 74)
        y = body(d, FW, FM, y + 34, "O dado sai do seu controle — e vai para a base de uma empresa terceira, muitas vezes no exterior.", 42)
        footer(img, d, FW, FH, FM, "swipe")
    def s3(img, d, y):
        y = headline(d, FW, FM, y + 8, "Sigilo: dever absoluto.", 84)
        y += 36
        y = panel(d, y, [
            "Art. 34 — Estatuto da Advocacia",
            "Violação mesmo sem vazamento",
            "Basta o dado sair do seu controle",
        ], tintB, kind="warn", item_size=37)
        footer(img, d, FW, FH, FM, "swipe")
    def s4(img, d, y):
        y = headline(d, FW, FM, y + 8, "LGPD: o escritório é o controlador.", 80)
        y += 36
        y = panel(d, y, [
            "Multa: até 2% do faturamento",
            "Teto: R$ 50 milhões por infração",
            "ANPD: fiscalização reforçada em 2026",
        ], tintR, kind="warn", item_size=37)
        footer(img, d, FW, FH, FM, "swipe")
    def s5(img, d, y):
        y = headline(d, FW, FM, y + 8, "Transparência: cliente informado por escrito.", 76)
        y = body(d, FW, FM, y + 34, "Recomendação 001/2024, item 4 — antes de usar IA no caso. E ele pode recusar.", 42)
        footer(img, d, FW, FH, FM, "swipe")
    def s6(img, d, y):
        y = headline(d, FW, FM, y + 8, "O chat não é cofre.", 88)
        y = body(d, FW, FM, y + 34, "Pelo Marco Civil da Internet, o histórico das suas conversas pode ser requisitado por ordem judicial.", 42)
        footer(img, d, FW, FH, FM, "swipe")
    def s7(img, d, y):
        y = headline(d, FW, FM, y + 8, "O protocolo em 4 passos.", 84)
        y += 36
        y = panel(d, y, [
            "Ferramenta com DPA",
            "Anonimização — [CLIENTE], [CPF], [VALOR]",
            "Cláusula no contrato",
            "Política interna do escritório",
        ], tintG, numbered=True, item_size=36)
        footer(img, d, FW, FH, FM, "swipe")
    def s8(img, d, y):
        y = headline(d, FW, FM, y + 10, "A produtividade fica. O risco sai.", 90)
        y = body(d, FW, FM, y + 30, "A implementação completa dos 4 passos está no nosso site.", 44, PAPER)
        footer(img, d, FW, FH, FM, "cta")

    slide(1, "LGPD & SIGILO", s1)
    slide(2, "O PROBLEMA", s2)
    slide(3, "FRENTE 1 · SIGILO", s3)
    slide(4, "FRENTE 2 · LGPD", s4)
    slide(5, "FRENTE 3 · TRANSPARÊNCIA", s5)
    slide(6, "O DETALHE QUE NINGUÉM VÊ", s6)
    slide(7, "O PROTOCOLO", s7)
    slide(8, "O RESULTADO", s8)

# ================================================================ main
if __name__ == "__main__":
    a1(); a1_story(); a2(); a2_story(); a3(); a3_story(); a4(); a5(); a6()
    serie_b(); serie_c()
    serie_d("instagram-carrossel-lgpd-sigilo", mono=False)
    serie_d("instagram-carrossel-lgpd-sigilo-v2", mono=True)
    print("\nconcluído.")
