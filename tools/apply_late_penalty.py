#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import math
from datetime import datetime

def iso_to_dt(s: str) -> datetime:
    s = s.replace("Z", "+00:00")
    return datetime.fromisoformat(s)

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--due", required=True)
    ap.add_argument("--now", required=True)
    ap.add_argument("--per-day", type=float, default=0.10)
    ap.add_argument("--max", dest="max_penalty", type=float, default=0.50)
    ap.add_argument("--results-b64", required=True)
    args = ap.parse_args()

    due = iso_to_dt(args.due)
    now = iso_to_dt(args.now)

    late_seconds = (now - due).total_seconds()
    days_late = 0 if late_seconds <= 0 else math.ceil(late_seconds / 86400)
    penalty = min(args.max_penalty, args.per_day * days_late)
    factor = 1.0 - penalty

    raw_json = base64.b64decode(args.results_b64).decode("utf-8")
    results = json.loads(raw_json)

    if "tests" in results and isinstance(results["tests"], list):
        for t in results["tests"]:
            if "score" in t and isinstance(t["score"], (int, float)):
                t["score"] = round(float(t["score"]) * factor, 2)

    msg = results.get("message")
    penalty_line = f"Late penalty applied: {int(penalty*100)}% ({days_late} day(s) late)."
    results["message"] = (msg + " | " + penalty_line) if msg else penalty_line

    compact = json.dumps(results, separators=(",", ":"))
    out_b64 = base64.b64encode(compact.encode("utf-8")).decode("ascii")
    print(out_b64)

if __name__ == "__main__":
    main()
