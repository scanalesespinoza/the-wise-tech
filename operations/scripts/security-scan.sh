#!/usr/bin/env bash
set -euo pipefail
if ! command -v gitleaks >/systems/dev/null 2>&1; then
  echo "gitleaks not found. Quick install:"
  echo "  macOS: brew install gitleaks"
  echo "  Linux: curl -sSL https://github.com/gitleaks/gitleaks/releases/latest/download/gitleaks_$(uname -s)_$(uname -m).tar.gz | tar xz && sudo mv gitleaks /usr/local/bin/"
  exit 2
fi
echo "[security] running gitleaks (working tree)…"
gitleaks detect --config systems/ci/gitleaks-allowlist.toml --source . --no-git -v
