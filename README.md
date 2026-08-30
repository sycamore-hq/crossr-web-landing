# crossr-web-landing

Public front door for CrossR. Links out to the three products. Owns no skill law, no loop law, no harness spec.

**Door:** https://sycamore-hq.github.io/crossr-web-landing/  
The leftover https://sycamore-hq.github.io/crossr-skills/ is replaced by a moved stub (web-06).

**Charter:** [`docs/plans/crossr-web-landing-cut.html`](docs/plans/crossr-web-landing-cut.html) ([markdown](docs/plans/crossr-web-landing-cut.md)).

See [MIGRATION.md](MIGRATION.md).

- [crossr-skills](https://github.com/sycamore-hq/crossr-skills) — catalog (`skills = "v0-last-monolith"`)
- [crossr-loops](https://github.com/sycamore-hq/crossr-loops) — AVRIL / AXEL / BRICK / GAN (`loops = "v0"`)
- [crossr-harness](https://github.com/sycamore-hq/crossr-harness) — spec, bootstrap, dashboard (`v0`)

Split charter: [`skills-loops-harness-split.html`](https://github.com/sycamore-hq/crossr-skills/blob/main/docs/plans/skills-loops-harness-split.html).

## What's here

- `site/` — Zola door. `base_url` is this remote's Pages host.
- `book/` — mdBook TOC with links only (catalog → skills, pipeline → loops, bootstrap → harness). Not a second spec.
- `docs/plans/` — this door's charter.

## Pages

Enabled on this remote via GitHub Actions. Host: `https://sycamore-hq.github.io/crossr-web-landing/`. Custom domain: none. Do not invent one.

## Not here

- `SKILL.md`
- `HARNESS-SPEC.md`
- Loop law (AVRIL / AXEL / BRICK)
