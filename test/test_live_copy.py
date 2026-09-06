#!/usr/bin/env python3
"""Prove live-copy checks catch 5g defects and pass on current copy.

Fixture tests pin the calculations. The live-tree test is the door gate.
"""

import importlib.machinery
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_loader(
    "live_copy",
    importlib.machinery.SourceFileLoader(
        "live_copy", str(ROOT / "scripts" / "live_copy.py")
    ),
)
live_copy = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(live_copy)

STALE_HTML = """
<p>AVRIL, AXEL, BRICK conductor, rust-team-lead. Pin v0 does not include graphs.</p>
<p>Pins skills = v0-last-monolith, loops = v0. Never overwrites .opencode/.</p>
<div class="skill-pill rounded-2xl px-5 py-4"><div class="font-semibold">code-writer</div></div>
<div class="skill-pill rounded-2xl px-5 py-4"><div class="font-semibold">rust-code-writer</div></div>
<div class="skill-pill rounded-2xl px-5 py-4"><div class="font-semibold">rust-code-reviewer</div></div>
<div class="skill-pill rounded-2xl px-5 py-4"><div class="font-semibold">agent-harness</div></div>
<div class="skill-pill rounded-2xl px-5 py-4"><div class="font-semibold">skill-evaluator</div></div>
<div>skills = "v0-last-monolith"</div>
<div>loops  = "v0"</div>
"""

CLEAN_HTML = """
<p>AVRIL, AXEL, BRICK conductor, code-gan graph. Topology, not a runtime.</p>
<p>Pins skills = v1-gan-layers, loops = v1-cards. Generates .opencode/agent/.</p>
<div class="skill-pill rounded-2xl px-5 py-4"><div class="font-semibold">code-writer</div></div>
<div class="skill-pill rounded-2xl px-5 py-4"><div class="font-semibold">rust</div></div>
<div class="skill-pill rounded-2xl px-5 py-4"><div class="font-semibold">code-review</div></div>
<div class="skill-pill rounded-2xl px-5 py-4"><div class="font-semibold">agent-harness</div></div>
<div class="skill-pill rounded-2xl px-5 py-4"><div class="font-semibold">skill-evaluator</div></div>
<div>skills = "v1-gan-layers"</div>
<div>loops  = "v1-cards"</div>
"""


class TokenHits(unittest.TestCase):
    def test_finds_retired_full_names(self):
        text = "drop rust-team-lead and rust-code-writer from the door"
        self.assertEqual(
            live_copy.token_hits(text, live_copy.RETIRED_NAMES),
            ("rust-team-lead", "rust-code-writer"),
        )

    def test_rust_book_is_not_rust_code_writer(self):
        text = "language books (rust, ocaml) and the rust book"
        self.assertEqual(live_copy.token_hits(text, live_copy.RETIRED_NAMES), ())

    def test_misses_absent_names(self):
        self.assertEqual(
            live_copy.token_hits("AVRIL, AXEL, BRICK conductor", live_copy.RETIRED_NAMES),
            (),
        )


class FeaturedPills(unittest.TestCase):
    def test_reads_pills_in_order(self):
        self.assertEqual(
            live_copy.featured_pill_names(CLEAN_HTML),
            live_copy.FEATURED_PILLS,
        )

    def test_stale_pills_are_the_old_writers(self):
        names = live_copy.featured_pill_names(STALE_HTML)
        self.assertIn("rust-code-writer", names)
        self.assertIn("rust-code-reviewer", names)
        self.assertNotEqual(names, live_copy.FEATURED_PILLS)


class PinAssignments(unittest.TestCase):
    def test_reads_quoted_and_bare_values(self):
        text = 'skills = "v1-gan-layers"\nloops  = v1-cards\n'
        self.assertEqual(
            live_copy.pin_assignments(text),
            (("skills", "v1-gan-layers"), ("loops", "v1-cards")),
        )

    def test_stale_snippet_is_v0(self):
        assigns = live_copy.pin_assignments(STALE_HTML)
        self.assertIn(("skills", "v0-last-monolith"), assigns)
        self.assertIn(("loops", "v0"), assigns)

    def test_backticked_bare_pin_drops_trailing_tick(self):
        self.assertEqual(
            live_copy.pin_assignments("`loops = v1-cards`"),
            (("loops", "v1-cards"),),
        )

    def test_v0_token_skips_semver_and_still_hits_pin_v0(self):
        self.assertIsNone(live_copy.V0_TOKEN.search("tag v0.1.0"))
        self.assertIsNotNone(live_copy.V0_TOKEN.search("Pin v0 does not include graphs."))
        self.assertIsNotNone(live_copy.V0_TOKEN.search("v0-last-monolith"))

    def test_pin_surface_fails_on_v0_and_passes_on_current(self):
        stale = 'catalog (`skills = "v0-last-monolith"`)\nloops = "v0"\n'
        clean = 'catalog (`skills = "v1-gan-layers"`)\nloops = "v1-cards"\n'
        stale_fails = live_copy.pin_surface_failures(stale)
        self.assertTrue(stale_fails)
        self.assertTrue(any("v0" in item for item in stale_fails))
        self.assertEqual(live_copy.pin_surface_failures(clean), ())


class HtmlFailures(unittest.TestCase):
    def test_stale_html_fails_every_5g_check(self):
        failures = live_copy.html_failures(STALE_HTML)
        joined = " ".join(failures)
        self.assertTrue(failures)
        self.assertIn("rust-team-lead", joined)
        self.assertIn("rust-code-writer", joined)
        self.assertIn("featured pills", joined)
        self.assertIn("v0", joined)
        self.assertIn("v1-gan-layers", joined)
        self.assertIn("v1-cards", joined)

    def test_clean_html_has_no_failures(self):
        self.assertEqual(live_copy.html_failures(CLEAN_HTML), ())

    def test_report_lines_pass_on_clean(self):
        self.assertEqual(
            live_copy.report_lines(CLEAN_HTML),
            ("live HTML copy is current",),
        )

    def test_report_lines_prefix_failures(self):
        lines = live_copy.report_lines(STALE_HTML)
        self.assertTrue(lines)
        self.assertTrue(all(line.startswith("FAIL: ") for line in lines))


class LiveTree(unittest.TestCase):
    def test_door_html_has_no_5g_failures(self):
        html = (ROOT / "site" / "templates" / "index.html").read_text()
        self.assertEqual(live_copy.html_failures(html), ())

    def test_cli_exits_zero_on_current_door(self):
        self.assertEqual(live_copy.main([]), 0)


class GateWiring(unittest.TestCase):
    def test_check_workflow_runs_the_suite(self):
        text = (ROOT / ".github" / "workflows" / "check.yml").read_text()
        self.assertIn("python3 -m unittest discover -s test -v", text)
        self.assertIn("scripts/live_copy.py", text)
        self.assertIn("permissions:\n  contents: read", text)

    def test_deploy_gate_runs_before_installs(self):
        text = (ROOT / ".github" / "workflows" / "deploy-site.yml").read_text()
        self.assertLess(text.find("Live-copy gate"), text.find("Install Zola"))

    def test_justfile_check_runs_the_suite(self):
        text = (ROOT / "justfile").read_text()
        self.assertIn("unittest discover", text)
        self.assertIn("scripts/live_copy.py", text)


if __name__ == "__main__":
    unittest.main()
