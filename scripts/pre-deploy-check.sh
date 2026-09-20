#!/usr/bin/env bash
set -euo pipefail

echo "Running pre-deployment validation..."
test -f README.md
test -d ansible
test -d kubernetes
test -d fabric
echo "Pre-deployment checks passed."
