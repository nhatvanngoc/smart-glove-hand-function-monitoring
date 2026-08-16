#!/usr/bin/env bash
# Install the official MiKTeX runtime on Debian 12 (Bookworm).
set -euo pipefail

EXPECTED_FINGERPRINT="D6BC243565B2087BC3F897C9277A7293F59E4889"
KEY_URL="https://miktex.org/download/key"
REPO_URL="https://miktex.org/download/debian"
KEYRING="/usr/share/keyrings/miktex.gpg"
SOURCE_LIST="/etc/apt/sources.list.d/miktex.list"

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  cat <<'EOF'
Usage: scripts/install_miktex_debian.sh

Installs MiKTeX from its official Debian 12 repository, verifies the signing-key
fingerprint, completes per-user setup, and enables automatic package install.
Requires sudo and working HTTPS access to Debian and miktex.org repositories.
EOF
  exit 0
fi
[[ $# -eq 0 ]] || { echo "Unknown argument: $1" >&2; exit 2; }

[[ -r /etc/os-release ]] || { echo "Cannot identify operating system." >&2; exit 1; }
# shellcheck disable=SC1091
. /etc/os-release
if [[ "${ID:-}" != "debian" || "${VERSION_CODENAME:-}" != "bookworm" ]]; then
  echo "This installer is intentionally limited to Debian 12 Bookworm; found ${PRETTY_NAME:-unknown}." >&2
  echo "Use the official installer at https://miktex.org/download for this OS." >&2
  exit 1
fi
command -v sudo >/dev/null || { echo "sudo is required." >&2; exit 1; }
sudo -v

# Install verification/download prerequisites before trusting the new repository.
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y ca-certificates curl gnupg

key_tmp="$(mktemp)"
trap 'rm -f "$key_tmp"' EXIT
curl --proto '=https' --tlsv1.2 --retry 5 --retry-all-errors \
  --connect-timeout 20 -fsSL "$KEY_URL" -o "$key_tmp"

actual_fingerprint="$(gpg --batch --show-keys --with-colons "$key_tmp" \
  | awk -F: '$1 == "fpr" { print $10; exit }')"
if [[ "$actual_fingerprint" != "$EXPECTED_FINGERPRINT" ]]; then
  echo "MiKTeX signing-key fingerprint mismatch." >&2
  echo "Expected: $EXPECTED_FINGERPRINT" >&2
  echo "Actual:   ${actual_fingerprint:-unavailable}" >&2
  exit 1
fi

sudo gpg --batch --yes --dearmor -o "$KEYRING" "$key_tmp"
echo "deb [signed-by=$KEYRING] $REPO_URL bookworm universe" \
  | sudo tee "$SOURCE_LIST" >/dev/null
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y miktex

# Per-user setup avoids writing the research user's TeX tree as root.
miktexsetup finish
initexmf --set-config-value='[MPM]AutoInstall=1'
initexmf --update-fndb

printf '\nMiKTeX runtime ready:\n'
miktexsetup --version | head -n 3
pdflatex --version | head -n 3
