# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary: strangers who arrive through a single article (search, a shared link, a repost) and want to know who wrote it and whether the rest of the blog is worth their time. They read in Chinese, mostly long-form: essays, fiction, short poems.

The About page answers that visitor's one question: who is this person. Friends, collaborators and the author's own archive are secondary readers, not the design target.

## Product Purpose

Coink's personal blog (coink.wang), running since 2015. A home for the author's own writing — essays, fiction (e.g. 「机不录」志怪集), poems, life notes and technical pieces — and a small self-portrait of the person behind it.

Success: a visitor finishes an article comfortably, and a visitor who opens About leaves with a clear, specific picture of the author's interests rather than a generic "about me" grid.

## Positioning

A hand-built, single-author blog whose theme is also made by the author ("Theme by myself"). Its recurring identity is birdwatching: the author birds in the field with a Nikon P950 and publishes the photography on 小红书.

## Operating Context

- Jekyll site deployed on GitHub Pages; layouts in `_layouts/`, includes in `_includes/`.
- Multiple swappable visual themes selected by `theme_style` in `_config.yml`; each theme lives in `_sass/<name>/` plus an optional `assets/fonts/<name>.css`.
- Readers are largely in mainland China: fonts are self-hosted because Google Fonts is blocked there; no external font CDNs.
- Comments via Waline on posts, self-hosted at comments.coink.wang (Vercel + Neon Postgres), anonymous comments allowed; analytics via Clicky.
- Posts carry `title`, `subtitle`, `tag` (life / fiction / poem / phil / tech / work), `date`, optional `alert`, and footnotes (`assets/js/footnotes.js`).

## Capabilities and Constraints

- Pages: home (paginated, grouped by year), post, tag pages, About, Friends (links), 404.
- Long-form Chinese reading must stay comfortable: decorative or pixel type is for interface, headings and About; article body text stays in a highly legible face.
- New visual directions ship as a new `theme_style`, leaving existing themes intact and switchable.
- About content is fixed for now (confirmed 2026-10-01): the eight interests (游戏, 观鸟, 写作, 阅读, 园艺, 健身, 音乐, 编码), the game and music lists, the published book with cover, the WIP title 失眠权, and the 小红书 link. Present it differently; do not add or remove facts.

## Brand Commitments

- Site title "Coink | DO BOOM!", author name Coink / CoinkWang.
- Birdwatching is the recurring motif across themes and must survive any redesign.
- Footer licence: CC BY-NC-SA 4.0; "Theme by myself".

## Evidence on Hand

- Book: 《黑客与安全技术指南》, 清华大学出版社, 2017 — cover image hosted at s2.loli.net.
- 小红书 profile with the author's bird photography.
- Unused front matter in `about.md` (`works`: Glance theme, the book, YouTube 双语字幕插件) — not shown by decision.
- No bird species list, testimonials, or photo set exists in the repo; do not fabricate them.

## Product Principles

1. The writing comes first; the theme frames it and never competes with a paragraph.
2. Specific over generic: name the actual games, bands, camera and birds, never stock hobby tiles.
3. Made by hand, visibly — the theme itself is part of the author's self-portrait.
4. Works where the readers are: self-hosted, light, fast on mainland networks.
