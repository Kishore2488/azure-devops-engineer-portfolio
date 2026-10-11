import json
import sys
from pathlib import Path

THRESHOLD = 75

def validate(payload: dict) -> int:
    required = ["release", "environment", "tables", "capacity_percent"]
    missing = [key for key in required if key not in payload]
    if missing:
        print(f"FAIL: missing fields: {', '.join(missing)}")
        return 1

    if not payload["tables"]:
        print("FAIL: no tables supplied for synchronization validation")
        return 1

    if payload["capacity_percent"] > THRESHOLD:
        print(f"WARNING: capacity at {payload['capacity_percent']}% (threshold {THRESHOLD}%)")

    stale = [t["name"] for t in payload["tables"] if not t.get("synchronized", False)]
    if stale:
        print("FAIL: unsynchronized tables:", ", ".join(stale))
        return 1

    print(f"PASS: {payload['release']} / {payload['environment']}")
    print(f"PASS: {len(payload['tables'])} tables synchronized")
    return 0

if __name__ == "__main__":
    sys.exit(validate(json.loads(Path(sys.argv[1]).read_text())))
