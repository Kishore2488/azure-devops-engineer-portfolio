#!/usr/bin/env bash
set -euo pipefail

echo "Running lightweight portfolio security checks..."

if grep -RInE 'AKIA[0-9A-Z]{16}|-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----' .   --exclude-dir=.git --exclude='*.md'; then
  echo "FAIL: possible credential material detected"
  exit 1
fi

if grep -RInE 'password[[:space:]]*[:=][[:space:]]*["'"'][^"'"']+["'"']' .   --exclude-dir=.git --exclude='*.md'; then
  echo "FAIL: possible hardcoded password detected"
  exit 1
fi

echo "PASS: no obvious credential patterns found"
