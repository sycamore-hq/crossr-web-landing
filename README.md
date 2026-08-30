# crossr-web-landing

Public front door for CrossR. Links out to the three products. Owns no skill law, no loop law, no harness spec.

**Extract in progress (split-05).** Zola `site/` copied from `sycamore-hq/crossr-skills`. mdBook rewritten as **links**. See [MIGRATION.md](MIGRATION.md).

- [crossr-skills](https://github.com/sycamore-hq/crossr-skills) — catalog
- [crossr-loops](https://github.com/sycamore-hq/crossr-loops) — AVRIL / AXEL / BRICK / GAN
- [crossr-harness](https://github.com/sycamore-hq/crossr-harness) — spec, bootstrap, dashboard

Charter: [`skills-loops-harness-split.html`](https://github.com/sycamore-hq/crossr-skills/blob/main/docs/plans/skills-loops-harness-split.html).

## What's here

- `site/` — Zola marketing site, byte-identical copy. `base_url` still names the skills Pages host; live Pages stay on skills until the cut.
- `book/` — mdBook TOC with links only (catalog → skills, pipeline → loops, bootstrap → harness). Not a second spec.

## Not here

- `SKILL.md`
- `HARNESS-SPEC.md`
- Loop law (AVRIL / AXEL / BRICK)
- Deploy workflow (Pages still ship from `crossr-skills`)
