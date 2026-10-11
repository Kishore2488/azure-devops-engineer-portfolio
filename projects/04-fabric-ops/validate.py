import json
import sys

with open(sys.argv[1], encoding="utf-8") as handle:
    payload = json.load(handle)

required = {"workspace", "environment", "capacity_percent", "tables"}
missing = required - set(payload)
if missing:
    raise SystemExit("Missing: " + ", ".join(sorted(missing)))

if payload["capacity_percent"] >= 75:
    print("WARNING: capacity >= 75%")

failed = [item["name"] for item in payload["tables"] if not item.get("synchronized")]
if failed:
    raise SystemExit("Unsynchronized: " + ", ".join(failed))

print("PASS: Fabric release validation")
