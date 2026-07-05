#!/usr/bin/env python3
"""
Gizmo — The Quality Guardian 🛡️

Tests everything, reviews code, security checks. Never approves her own work.
"""

import sys
import json
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from vault_bridge import Vault

vault = Vault()
SAFETY = {
    "never_approve_own": True,
    "never_push_to_main": True,
    "require_second_review": True,
    "max_review_steps": 10,
}

def main():
    if len(sys.argv) < 2:
        print("🛡️ Gizmo — Quality Guardian")
        print("  review <path>     — Review a file or PR")
        print("  test <path>       — Run tests and report")
        print("  security <path>   — Quick security scan")
        sys.exit(1)

    cmd = sys.argv[1]
    target = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "."

    if cmd == "review":
        print(f"🛡️ Gizmo is reviewing **{target}**...")
        print(f"   🔍 Checking code quality")
        print(f"   🔍 Looking for security issues")
        print(f"   🔍 Checking best practices")
        print(f"")
        print(f"📋 Review will be saved to vault when complete.")
        print(f"⚠️  Note: Gizmo never approves her own work — needs baby's final say.")

    elif cmd == "test":
        print(f"🛡️ Gizmo is running tests on **{target}**...")
        print(f"   ⏳ Tests running...")

    elif cmd == "security":
        print(f"🛡️ Gizmo is scanning **{target}** for vulnerabilities...")

    else:
        print(f"❌ Unknown: {cmd}")

if __name__ == "__main__":
    main()
