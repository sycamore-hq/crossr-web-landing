# Bootstrapping a New Project

The bootstrap script's home is [`crossr-harness`](https://github.com/sycamore-hq/crossr-harness) (`scripts/harness-bootstrap`). Spec: [HARNESS-SPEC.md](https://github.com/sycamore-hq/crossr-harness/blob/main/HARNESS-SPEC.md).

```bash
git clone https://github.com/sycamore-hq/crossr-harness.git
./crossr-harness/scripts/harness-bootstrap /path/to/your-new-project
```

Pins (see the harness `lockfile.toml`):

```
skills = "v0-last-monolith"
loops  = "v0"
```

Full install copies catalog skills, loop conductors + personas + `/avril` `/axel`, and harness templates. Never overwrites existing `.opencode/`. No git submodules.

`--process-only` writes tracking files without copying skills (how the three product remotes consume the harness).

`graphs/` live on [`crossr-loops` `main`](https://github.com/sycamore-hq/crossr-loops/tree/main/graphs). They are **not** in pin `v0`. Bootstrap does not copy them. Topology only — if a graph and a `SKILL.md` disagree, the skill wins.

The old `crossr-skills/scripts/harness-bootstrap` is a shim: it prints `deprecated: use sycamore-hq/crossr-harness` and exits 1.

This landing page does not own the script or the spec.
