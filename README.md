# crossr-web-landing

Public front door for CrossR. Links out to the three products. Owns no skill law, no loop law, no harness spec.

**The live Pages URL is stale.** https://sycamore-hq.github.io/crossr-skills/ is the frozen pre-cut site (one repo, 25 skills, Eternal Forge). This remote's Pages is still off.

**Charter:** [`docs/plans/crossr-web-landing-cut.html`](docs/plans/crossr-web-landing-cut.html) ([markdown](docs/plans/crossr-web-landing-cut.md)). Next unit: web-01 after the charter is blessed.

See [MIGRATION.md](MIGRATION.md).

- [crossr-skills](https://github.com/sycamore-hq/crossr-skills) — catalog (`skills = "v0-last-monolith"`)
- [crossr-loops](https://github.com/sycamore-hq/crossr-loops) — AVRIL / AXEL / BRICK / GAN (`loops = "v0"`)
- [crossr-harness](https://github.com/sycamore-hq/crossr-harness) — spec, bootstrap, dashboard (`v0`)

Split charter: [`skills-loops-harness-split.html`](https://github.com/sycamore-hq/crossr-skills/blob/main/docs/plans/skills-loops-harness-split.html).

## What's here

- `site/` — Zola marketing site. `base_url` still names the skills Pages host (web-01 rewrites copy; web-05 rewrites host).
- `book/` — mdBook TOC with links only (catalog → skills, pipeline → loops, bootstrap → harness). Not a second spec.
- `docs/plans/` — this door's charter.

## Pages

Not enabled on this remote. Last skills deploy is frozen (workflow removed in split-07). Custom domain: none. Do not invent one.

## Not here

- `SKILL.md`
- `HARNESS-SPEC.md`
- Loop law (AVRIL / AXEL / BRICK)
- Deploy workflow (web-05)
