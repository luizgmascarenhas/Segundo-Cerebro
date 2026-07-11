# AGENTS.md

This repo is a **personal Obsidian vault** (one git repo, remote `github.com/luizgmascarenhas/Segundo-Cerebro.git`, branch `main`), not a software codebase. It mixes Markdown/PDF notes (PARA method: `PROJETOS/`, `RECURSOS/`, `ARQUIVOS/`) with a few embedded code projects. There is **no build/test/lint tooling at this level** — most tasks are content authoring in Portuguese (BR).

## Nested repos — read before any git operation

This is the single easiest way to get confused here. Verify which repo a path belongs to before committing:

- **`PROJETOS/mlassessoria` is a dangling gitlink** (mode `160000`) with **no `.gitmodules`**. Its contents are NOT in this repo and won't appear on a fresh clone. Treat it as out of scope; don't try to `git add` files inside it from here.
- **`PROJETOS/uso de ia no direito/lp/` is a fully independent git repo** (its own `.git` and remote `github.com/luizgmascarenhas/ia-advocacia.git`). It is tracked **zero** by this repo. Changes inside `lp/` are invisible to `git status`/commits run from here — `cd lp/` and use its own git. A separate `AGENTS.md` lives in `lp/` and applies there.

Always run `git status` from the directory you intend to commit.

## Where work happens

- **Content product (e-book "IA na advocacia")** → `PROJETOS/uso de ia no direito/`. Read its `CLAUDE.md` first: it defines the base files, tone-of-voice, legal-citation requirements (must cite OAB Recomendação 001/2024, LGPD Lei 13.709/2018, Estatuto Lei 8.906/1994), and the 3 risk areas (sigilo, alucinações, transparência). All copy is Portuguese (BR); never use hype words ("truque", "hack", "revolucionário").
- **Vault-wide guidance** → `PROJETOS/CLAUDE.md` (PARA layout, Obsidian conventions).

Do not duplicate these files here; defer to them for project-specific detail.

## The only code project: `lp/` (landing page)

Next.js **16** + React **19** + Tailwind **4** + TypeScript. Bleeding-edge versions — its `AGENTS.md` warns the APIs differ from training data, so read `node_modules/next/dist/docs/` before writing Next.js code. Run from inside `lp/`:

```
npm run dev      # dev server
npm run build    # production build
npm run lint     # eslint
```

`lp/`'s `CLAUDE.md` just contains `@AGENTS.md`.

## Instagram art generator

`PROJETOS/uso de ia no direito/scripts/gerar_artes_instagram.py` renders PNG carousels/reels with Pillow (`PIL`). Requires **Pillow** (verified 10.2.0 available). Outputs go to `instagram-imagens/`. Note: `ROOT` is **hardcoded to this machine's absolute path** (line ~13) and fonts are pulled from `.claude/skills/canvas-design/canvas-fonts` — update `ROOT` if running elsewhere.

## Conventions

- New/edited notes: Markdown + Obsidian frontmatter (`tags:`), Portuguese (BR).
- No conventional-commits standard is enforced (existing commits: "inicial", "Initial commit") — keep messages plain.
- Commits are to `main` directly; this is a personal vault, no PR/branch workflow observed.
