# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **content product development project**, not a software codebase. The goal is to create and refine a low-ticket digital product (e-book, R$97) teaching lawyers how to use AI tools while complying with OAB ethics rules and LGPD (Brazilian data protection law).

**Product promise:** "Usar IA na advocacia sem violar a OAB"
**Format:** PDF e-book, 30–50 pages
**Target buyer:** Brazilian lawyers (solo, small firm, or newly licensed) who want to adopt AI but fear OAB sanctions or LGPD violations

## Key Files and Their Roles

### Base files — read these first before any task

| File | Role |
|------|------|
| `concepcao-ia-advocacia-oab.md` | Product strategy foundation — 50 benefits, 5 buyer personas ("baldes"), 5 purchase objections with 7-argument framework each, consumer identity "Rafael Menezes", tone guide |
| `ia-na-advocacia-sem-violar-oab.md` | Core product content — the actual e-book in its condensed 3-action format, with checklists, copy-ready contract clause, curated tool list, and implementation plan |
| `recomendacao 001-2024 - oab.md` | Primary legal source — OAB Recomendação 001/2024 full text; canonical reference for all legal claims in the product |

### Supporting files

| File | Role |
|------|------|
| `ia-no-direito.md` | Expanded research draft — 6-chapter version with deeper citations; use as source material, not as the final product |
| `produto-ladeira.md` | Next deliverable — sales page / funnel copy (currently empty) |
| PDFs | Generated research and drafts; reference only, do not edit |

## Content Architecture

The product is built around **3 core risk areas** for lawyers using AI:
1. **Sigilo / LGPD** — client data leaking into AI training (solved by: anonymization + enterprise-tier tools)
2. **Alucinações** — fabricated case law (solved by: user-supplied sources only + mandatory verification)
3. **Transparência** — undisclosed AI use to clients (solved by: contract clause + informed consent)

These map directly to three OAB duties from Recomendação 001/2024: **sigilo, veracidade, transparência**.

## Installed Skills

Five Claude Code skills are installed in `.claude/skills/`. Use them via `/` commands:

- **brainstorming** — generating new angles, headline variants, content ideas
- **using-superpowers** — agentic workflows and multi-step tasks
- **product-strategist** — strategic framing, OKR generation (`scripts/okr_cascade_generator.py`)
- **product-manager-toolkit** — PRD templates, customer interview analysis, RICE prioritization
- **marketing-ideas** — campaign angles, channel strategy, copy hooks

## Working Conventions

- All content is in **Portuguese (Brazilian)**; maintain this in any additions or rewrites
- Legal references must cite actual sources: OAB Recomendação 001/2024, LGPD (Lei 13.709/2018), Estatuto da Advocacia (Lei 8.906/1994), Art. 77 CPC
- When drafting copy, mirror the tone defined in `concepcao-ia-advocacia-oab.md` §"Como se comunicar": técnico e confiável, embasado em lei, respeita o tempo do advogado — never "truque", "hack", "revolucionário"
- Buyer personas are defined in detail in `concepcao-ia-advocacia-oab.md` — use them to calibrate tone per audience segment
- `produto-ladeira.md` is the next major deliverable (sales page); it is currently empty
