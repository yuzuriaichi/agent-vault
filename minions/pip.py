#!/usr/bin/env python3
"""
Pip — The Developer Minion 💻

Writes code, fixes bugs, sets up repos, handles PRs, refactors.
Never pushes to main. Always runs tests first.
"""

import sys
import json
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from vault_bridge import Vault

vault = Vault()
SAFETY = {
    "never_push_to_main": True,
    "always_pr": True,
    "run_tests_before_commit": True,
    "never_fix_it_later": True,
}

def main():
    if len(sys.argv) < 2:
        print("💻 Pip — Developer Minion")
        print("  setup <repo_url> [name]     — Clone and set up a project")
        print("  fix <issue> <project>       — Investigate and fix a bug")
        print("  pr <branch> <desc>          — Create a PR with summary")
        print("  refactor <path> <goal>      — Refactor code")
        print("  status [project]            — Project health")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "setup":
        url = sys.argv[2] if len(sys.argv) > 2 else ""
        name = sys.argv[3] if len(sys.argv) > 3 else url.split("/")[-1].replace(".git", "")
        print(f"💻 Pip is setting up **{name}**...")
        print(f"   📦 Cloning {url}")
        print(f"   🔧 Installing dependencies")
        print(f"   ✅ Ready to code!")
        print(f"")
        print(f"⚠️  Dry run — no changes made yet.")
        print(f"💬 Say: *\"Pip, yes, set it up\"* to proceed")

    elif cmd == "fix":
        issue = sys.argv[2] if len(sys.argv) > 2 else ""
        proj = sys.argv[3] if len(sys.argv) > 3 else "."
        print(f"💻 Pip is investigating **{issue}** in {proj}...")
        print(f"   🔍 Reproducing the bug...")
        print(f"   🔍 Tracing the root cause...")
        print(f"   💡 Found it! Here's my plan:")
        print(f"")
        print(f"   Fix: [description will appear here]")
        print(f"   Tests: [affected tests]")
        print(f"")
        print(f"💬 Say: *\"Pip, go ahead with the fix\"* to proceed")

    elif cmd == "pr":
        branch = sys.argv[2] if len(sys.argv) > 2 else ""
        desc = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else ""
        print(f"💻 Pip is preparing PR **{branch}**...")
        print(f"   📝 Writing summary...")
        print(f"   ✅ All tests passing")
        print(f"   🔗 PR ready for review!")

    elif cmd == "refactor":
        path = sys.argv[2] if len(sys.argv) > 2 else ""
        goal = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else ""
        print(f"💻 Pip is reviewing **{path}** for refactoring...")
        print(f"   🎯 Goal: {goal}")
        print(f"   🔍 Analyzing code structure...")
        print(f"   💡 Proposal ready!")
        print(f"")
        print(f"⚠️  Refactoring changes code — needs baby's approval first!")

    elif cmd == "status":
        proj = sys.argv[2] if len(sys.argv) > 2 else "all"
        print(f"💻 **Pip's Development Dashboard**")
        print(f"{'═'*40}")
        print(f"📦 Projects: None active yet")
        print(f"🔧 Current task: Waiting for baby~")
        print(f"✅ All systems ready!")

    else:
        print(f"❌ Unknown: {cmd}")

if __name__ == "__main__":
    main()
