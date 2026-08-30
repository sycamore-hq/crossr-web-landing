# Update the CrossR door to match the cut

**Status:** proposed (web-00). Not executed.
**Human artifact:** [crossr-web-landing-cut.html](crossr-web-landing-cut.html)
**Live lie:** https://sycamore-hq.github.io/crossr-skills/ is the frozen pre-cut site.

Do not rewrite AVRIL/AXEL/BRICK `SKILL.md`. Do not copy loop law or HARNESS-SPEC into this remote. Do not invent a custom domain.

---

## Resume in a later session

1. Work from `sycamore-hq/crossr-web-landing` `main`.
2. Read this file + the HTML.
3. Split-00..09 is done. This is a **new chain**, not split-10.
4. Next unit is **web-01 (copy truth)** after this charter is blessed.

Trigger: “continue the landing update from web-01”.

---

## Why

The only public URL still works, and it is wrong.

It sells one repo (`scull7/crossr-skills`), 25 public skills, featured conductors (`avril`, `axel`, `rust-team-lead`), bootstrap from a script that now **exits 1**, Eternal Forge chrome (hammer + cross, Colossians 3:23), and `base_url` on a 404 host.

The cut is done. The door is not.

---

## Locked decisions

- **This remote is the CrossR product door**, under house **Sycamore HQ**. It is not a Sycamore org site. **Berea stays off this door.**
- Landing **links**. Owns no skill law, no loop law, no harness spec. Book stays a door.
- **No custom domain.** Host (when enabled): `https://sycamore-hq.github.io/crossr-web-landing/`.
- **House posture on the public door:** do not hide the belief, do not flaunt it. No cross in the mark. No verse in the footer. No Eternal Forge leftovers (hammer, flame-as-brand, “forged in the Cross”). Product README About lines are out of scope.
- **Mark:** Ficus sycomorus, low crown. Not Platanus. Palette: Well pitch `#171412`, Plaster page `#F3EEE6`, Packed mile `#C4A882`, Split fig `#9E4E36`, Dust leaf `#6A7348`, Canopy shade `#2E342C`. Motto: “Height enough.”
- **Zola + mdBook stay.** Zola is the root. mdBook at `/docs`. Combined build as before (`mdbook` → `site/static/docs`, then `zola build`).
- **Catalog count and featured list** are not invented here. Featured pills = `docs/public-skills.json` `featured` (today: `code-writer`, `rust-code-writer`, `rust-code-reviewer`, `agent-harness`, `skill-evaluator`). Count N=18 with a link to the allowlist. Do not vendor the JSON.
- **Conductors are loops**, not catalog pills. Pipeline section tells Intent → AVRIL → AXEL → Done and links to `crossr-loops`. BRICK is the alternative, not a flagship node.
- **Graphs:** one topology pointer to `crossr-loops/graphs/`. Not a runtime. If a graph and a `SKILL.md` disagree, the skill wins. Do not copy `graphs/*.json` into this remote.
- **Bootstrap snippet** clones `sycamore-hq/crossr-harness` and runs `./crossr-harness/scripts/harness-bootstrap`. Pins: `skills = "v0-last-monolith"`, `loops = "v0"`. Do not claim graphs are installed (they are not in pin `v0`).
- **Leftover Pages:** the frozen skills host keeps lying until a stub or takedown. Named unit **web-06**. Recommended: a one-page “moved” stub on skills Pages pointing here. Do not re-enable the old marketing tree on skills.
- Stacked PRs, < 10 min deep review. Acyclic deps unchanged: harness → loops → skills. Landing still owns no law.

---

## Freeze (this chain)

- No custom domain.
- No SKILL.md, no HARNESS-SPEC, no conductor copy.
- No graph runner. No new loops tag.
- No TanStack app. No preview host. Auth/db off.
- Do not rename the repo in this chain (URL stays `/crossr-web-landing/`).
- Do not put Berea on the door.

---

## What's stale (inventory)

| Surface | Today | After |
|---------|-------|-------|
| Live URL | `sycamore-hq.github.io/crossr-skills/` frozen Eternal Forge | This remote's Pages, once web-05 |
| `site/config.toml` | `base_url` `scull7.github.io/crossr-skills`; github `scull7/crossr-skills`; Eternal Forge palette | `sycamore-hq.github.io/crossr-web-landing`; github org; house palette |
| Hero | “ETERNAL FORGE • Forged in the Cross”; 25 skills | CrossR under Sycamore. Four remotes. N=18 |
| Featured pills | includes `avril`, `axel`, `rust-team-lead` | catalog `featured` only |
| Bootstrap | `git clone scull7/crossr-skills` + `./crossr-skills/scripts/harness-bootstrap` (shim, exit 1) | clone `crossr-harness`, run its bootstrap |
| Footer | Colossians 3:23; hammer-cross icon | no verse; house mark |
| `site/static/brand/*` | hammer + cross + flame JPGs, forge guide/palette | low-crown fig; rewrite or unpublish guide/palette |
| Book `getting-started/bootstrap.md` | “until dual-publish, run from the monolith” | harness clone; dual-publish is over |
| Book `harness/{html-first,stacked-prs}.md` | links to skills `book/` **deleted in split-07** | harness spec only |
| GitHub About | “Extract in progress. Not ready.” | Public front door. Owns no law. |
| This remote Pages | off | on in web-05 |
| Workflow | none | restore deploy pattern from `v0-last-monolith` |

---

## Units

| ID | What | Review target |
|----|------|----------------|
| **web-00** | This charter. README pointer. Pages still off. | this HTML + md |
| **web-01** | Copy truth on the Zola door. Four remotes, N=18, featured = catalog featured, bootstrap from harness, sycamore-hq URLs. **Keep current palette** so the review is copy, not brand. | `site/templates/index.html` + `config.toml` URLs |
| **web-02** | Book honesty. Fix bootstrap.md, dangling skills-book links, graphs pointer, GitHub About blurb. | `book/src/getting-started/bootstrap.md` |
| **web-03** | House visual system. Palette, drop Eternal Forge chrome and verse. CSS/SVG placeholder mark. Unpublish or rewrite `brand/guide.html` + `palette.html` so they cannot ship forge leftovers. | hero + footer + CSS variables |
| **web-04** | Real mark + assets. Low crown Ficus sycomorus. Favicon, logos, OG/GitHub banners. Remove hammer-cross JPGs from the public tree. | `site/static/brand/` |
| **web-05** | Host. Workflow (Zola + mdBook → Pages). `base_url`. Enable Actions Pages on this remote. No custom domain. | `.github/workflows/deploy-site.yml` |
| **web-06** | Frozen leftover. Skills Pages becomes a moved stub (recommended) or is disabled. Do not resurrect `site/` on skills. | tiny skills workflow or Pages setting |

**web-00 is this PR.** Stop after it lands unless told to continue.

---

## Not this chain

- Graph runner. Rhai. OpenCode-native graphs.
- New loops tag so pin `v0` includes `graphs/`.
- Custom domain.
- Berea.
- Rewriting product README faith lines.
- Re-adding orchestration skills to the catalog.

---

## Unresolved

1. **Pages path.** Default: keep repo name → `https://sycamore-hq.github.io/crossr-web-landing/`. Shorter `/crossr/` needs a rename or a different Pages repo — not this chain.
2. **Leftover skills Pages.** Default: moved stub (web-06). Alternative: disable and 404.
3. **House posture on the door.** Default: no verse, no cross in the mark. Alternative: keep a quiet CrossR product line on the hero (not recommended; contradicts house posture).
4. **Mark commissioning.** Default: placeholder in web-03, real assets in web-04 (generate or supply). Alternative: block visual ship on human art.
5. **Enable Pages this chain?** Default: **yes** (web-05). Otherwise the public URL keeps lying.

If any default is wrong, say so before web-01.
