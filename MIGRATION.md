# Migration

Clean copy from [`sycamore-hq/crossr-skills`](https://github.com/sycamore-hq/crossr-skills).
History stays on skills. This remote is a snapshot plus new work.

| Field | Value |
|-------|-------|
| Source remote | `sycamore-hq/crossr-skills` |
| Source SHA | `9ff577e6c2279bf4f0d0617417fb094e322985d5` (`main` at copy, after split-04) |
| Unit | split-05 |
| Method | clean copy of `site/` (byte-identical). `book/` rewritten as links — not a second spec. |
| Skills copies | kept until split-07 (dual-publish, then delete) |

Do not treat this SHA as a lockfile pin. Landing owns no law and is not a pin target.

## Copied (byte-identical)

### Zola `site/` (17 files)

- `site/config.toml`
- `site/content/_index.md`
- `site/templates/index.html`
- `site/static/brand/` (logos, banners, palette, guide, brand video)

`base_url` and GitHub extra still name `scull7.github.io/crossr-skills` — left alone (no rewrite on copy day).

## Rewritten (not a copy)

mdBook is a door. Chapter bodies are links; SUMMARY TOC is unchanged.

- `book/book.toml` — title/urls point at this remote
- `book/src/SUMMARY.md` — byte-identical TOC
- `book/src/introduction.md` — four remotes
- `book/src/pipeline/{overview,avril,axel,brick}.md` → [`crossr-loops`](https://github.com/sycamore-hq/crossr-loops)
- `book/src/getting-started/bootstrap.md` → [`crossr-harness`](https://github.com/sycamore-hq/crossr-harness)
- `book/src/skills/overview.md` → [`crossr-skills`](https://github.com/sycamore-hq/crossr-skills)
- `book/src/harness/{overview,html-first,stacked-prs}.md` → [`crossr-harness`](https://github.com/sycamore-hq/crossr-harness)

## Intentionally not copied

- `SKILL.md` / `.agents/` — catalog and loops
- `HARNESS-SPEC.md`, bootstrap, dashboard — harness
- `.github/workflows/deploy-site.yml` — Pages still deploy from skills
- `justfile` — site/book recipes stay on skills until the cut
- Pipeline chapter *bodies* (law stays in loops; this book links)

## Consumers

Live marketing + docs URL remains https://sycamore-hq.github.io/crossr-skills/ until Pages move. This remote is not yet the public host.
