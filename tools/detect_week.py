#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
from datetime import datetime, timezone

WEEK_RE = re.compile(r"^weeks/(w\d{2})/")

def iso_to_dt(s: str) -> datetime:
    s = s.replace("Z", "+00:00")
    return datetime.fromisoformat(s)

def get_changed_files() -> list[str]:
    try:
        out = subprocess.check_output(
            ["git", "diff", "--name-only", "HEAD^", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
        )
        return [l.strip() for l in out.splitlines() if l.strip()]
    except Exception:
        return []

def main() -> None:
    cfg = json.load(open("deadlines.json", "r", encoding="utf-8"))
    weeks_cfg: dict[str, dict] = cfg["weeks"]

    changed = get_changed_files()
    touched_weeks = sorted({m.group(1) for f in changed if (m := WEEK_RE.match(f))})

    if len(touched_weeks) == 1:
        week = touched_weeks[0]
    elif len(touched_weeks) > 1:
        raise SystemExit(
            f"Your push touched multiple weeks: {touched_weeks}. "
            "Please submit changes for only one week per push."
        )
    else:
        now = iso_to_dt(os.environ.get("RUN_STARTED_AT", datetime.now(timezone.utc).isoformat()))
        future = []
        for w, info in weeks_cfg.items():
            due = iso_to_dt(info["due"])
            if due > now:
                future.append((due, w))
        week = sorted(future)[0][1] if future else sorted(weeks_cfg.keys())[-1]

    info = weeks_cfg[week]
    out = os.environ["GITHUB_OUTPUT"]
    with open(out, "a", encoding="utf-8") as f:
        f.write(f"week={week}\n")
        f.write(f"due={info['due']}\n")
        f.write(f"max_score={info.get('max_score', 100)}\n")

if __name__ == "__main__":
    main()
