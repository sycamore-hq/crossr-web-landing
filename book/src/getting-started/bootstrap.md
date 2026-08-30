# Bootstrapping a New Project

The bootstrap script's home is [`crossr-harness`](https://github.com/sycamore-hq/crossr-harness) (`scripts/harness-bootstrap`). Spec: [HARNESS-SPEC.md](https://github.com/sycamore-hq/crossr-harness/blob/main/HARNESS-SPEC.md).

Until the dual-publish tag (split-06), run it from the monolith:

```bash
git clone https://github.com/sycamore-hq/crossr-skills.git
./crossr-skills/scripts/harness-bootstrap /path/to/your-new-project
```

This landing page does not own the script or the spec.
