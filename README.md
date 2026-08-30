# crossr-web-landing

Public front door for CrossR. Links out to the three products. Owns no skill law, no loop law, no harness spec.

**Dogfood is live (split-08).** Product remotes consume [`crossr-harness`](https://github.com/sycamore-hq/crossr-harness) `v0`. **Graphs (split-09)** live in [crossr-loops `graphs/`](https://github.com/sycamore-hq/crossr-loops/tree/main/graphs) — topology, not a runtime; SKILL.md stays the law. Pin `loops = "v0"` does not include them. This remote still owns no law.

See [MIGRATION.md](MIGRATION.md).

- [crossr-skills](https://github.com/sycamore-hq/crossr-skills) — catalog (`skills = "v0-last-monolith"`)
- [crossr-loops](https://github.com/sycamore-hq/crossr-loops) — AVRIL / AXEL / BRICK / GAN (`loops = "v0"`)
- [crossr-harness](https://github.com/sycamore-hq/crossr-harness) — spec, bootstrap, dashboard (`v0`)

Charter: [`skills-loops-harness-split.html`](https://github.com/sycamore-hq/crossr-skills/blob/main/docs/plans/skills-loops-harness-split.html).

## What's here

- `site/` — Zola marketing site. `base_url` still names the skills Pages host.
- `book/` — mdBook TOC with links only (catalog → skills, pipeline → loops, bootstrap → harness). Not a second spec.

## Pages

Not enabled on this remote. Last skills deploy is frozen (workflow removed in split-07). Custom domain: none. Do not invent one.

## Not here

- `SKILL.md`
- `HARNESS-SPEC.md`
- Loop law (AVRIL / AXEL / BRICK)
- Deploy workflow
