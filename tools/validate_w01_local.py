#!/usr/bin/env python3
"""Local validation helper for instructors.

- Copies the reference solution into weeks/w01/answers.py
- Runs pytest for week 01
- Restores the student template afterwards

Usage:
  python tools/validate_w01_local.py
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W01 = ROOT / "weeks" / "w01"

def main() -> None:
    student = W01 / "answers_student_template.py"
    sol = W01 / "answers_solution.py"
    active = W01 / "answers.py"

    if not student.exists() or not sol.exists():
        raise SystemExit("Missing required files in weeks/w01/.")

    # Backup current answers.py
    backup = W01 / "answers.backup.py"
    shutil.copy2(active, backup)

    try:
        shutil.copy2(sol, active)
        subprocess.check_call(["python", "-m", "pip", "install", "-r", str(ROOT / "requirements.txt")])
        subprocess.check_call(["pytest", "-q", str(ROOT / "tests_bank" / "w01" / "quiz_tests.py")])
        print("\n✅ Week 01 passed locally using answers_solution.py")
    finally:
        # Restore student template
        shutil.copy2(student, active)
        backup.unlink(missing_ok=True)

if __name__ == "__main__":
    main()
