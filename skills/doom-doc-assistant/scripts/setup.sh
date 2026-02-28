#!/usr/bin/env bash
# Setup script for Kubernetes YAML validation
# Installs ruamel.yaml and kubeconform. Idempotent.

set -e

# Detect installation directories
USER_BIN="${HOME}/.local/bin"
mkdir -p "$USER_BIN"

# Add to PATH if not already present (for current session)
if [[ ":$PATH:" != *":$USER_BIN:"* ]]; then
  export PATH="$USER_BIN:$PATH"
fi

# -----------------------------------------------------------------------------
# Install ruamel.yaml (Python package)
# -----------------------------------------------------------------------------

echo "==> Installing ruamel.yaml (YAML 1.2 parser)..."

# Check if already installed
if python3 -c "import ruamel.yaml" 2>/dev/null; then
  VERSION=$(python3 -c "import ruamel.yaml; print(ruamel.yaml.__version__)" 2>/dev/null || echo "unknown")
  echo "    ✓ ruamel.yaml already installed: $VERSION"
else
  # Try user-level installation first (no sudo required)
  if pip3 install --user ruamel.yaml -q 2>/dev/null; then
    echo "    ✓ ruamel.yaml installed to user site-packages"
  elif pip3 install ruamel.yaml -q 2>/dev/null; then
    echo "    ✓ ruamel.yaml installed"
  else
    echo "    ⚠️  Warning: Could not install ruamel.yaml automatically"
    echo ""
    echo "    Manual installation required:"
    echo "    pip3 install --user ruamel.yaml"
    echo ""
    echo "    Or use a virtual environment:"
    echo "    python3 -m venv ~/.venv && source ~/.venv/bin/activate"
    echo "    pip install ruamel.yaml"
    exit 1
  fi
fi

# -----------------------------------------------------------------------------
# Install kubeconform (Go binary)
# -----------------------------------------------------------------------------

echo "==> Checking kubeconform..."

# Check if already in PATH
if command -v kubeconform &>/dev/null; then
  echo "    ✓ kubeconform already installed: $(kubeconform -v 2>&1 | head -1)"
else
  # Check user bin directory
  if [ -x "$USER_BIN/kubeconform" ]; then
    echo "    ✓ kubeconform already installed at $USER_BIN/kubeconform"
  else
    echo "    Installing kubeconform to $USER_BIN..."

    # Detect architecture
    ARCH=$(uname -m)
    case "$ARCH" in
      x86_64) ARCH="amd64" ;;
      aarch64|arm64) ARCH="arm64" ;;
      *) echo "    ⚠️  Unsupported architecture: $ARCH"; exit 1 ;;
    esac

    # Detect OS
    OS=$(uname -s | tr '[:upper:]' '[:lower:]')
    case "$OS" in
      linux) ;;
      darwin) OS="darwin" ;;
      *) echo "    ⚠️  Unsupported OS: $OS"; exit 1 ;;
    esac

    # Use latest release redirect (no API call needed)
    DOWNLOAD_URL="https://github.com/yannh/kubeconform/releases/latest/download/kubeconform-${OS}-${ARCH}.tar.gz"
    CHECKSUMS_URL="https://github.com/yannh/kubeconform/releases/latest/download/CHECKSUMS"

    echo "    Downloading from $DOWNLOAD_URL..."

    # Download to temp file for verification
    TMP_DIR=$(mktemp -d)
    TMP_ARCHIVE="$TMP_DIR/kubeconform.tar.gz"

    # Download binary and checksums
    if ! curl -sL "$DOWNLOAD_URL" -o "$TMP_ARCHIVE"; then
      echo "    ⚠️  Failed to download kubeconform"
      rm -rf "$TMP_DIR"
      exit 1
    fi

    if ! curl -sL "$CHECKSUMS_URL" -o "$TMP_DIR/CHECKSUMS"; then
      echo "    ⚠️  Warning: Could not download checksums for verification"
      echo "    Proceeding without checksum verification..."
    else
      # Verify checksum
      cd "$TMP_DIR"
      if sha256sum -c CHECKSUMS --ignore-missing 2>/dev/null | grep -q "kubeconform.tar.gz: OK"; then
        echo "    ✓ Checksum verification passed"
      else
        echo "    ⚠️  Warning: Checksum verification failed"
        echo "    The downloaded file may be corrupted or tampered with"
        rm -rf "$TMP_DIR"
        exit 1
      fi
    fi

    # Extract and install
    if tar xzf "$TMP_ARCHIVE" -C "$USER_BIN" kubeconform; then
      chmod +x "$USER_BIN/kubeconform"
      rm -rf "$TMP_DIR"
      echo "    ✓ kubeconform installed: $("$USER_BIN/kubeconform" -v 2>&1 | head -1)"
      echo ""
      echo "    ⚠️  Note: $USER_BIN is not in your PATH by default."
      echo "    Add this to your ~/.bashrc or ~/.zshrc:"
      echo "        export PATH=\"\$HOME/.local/bin:\$PATH\""
    else
      echo "    ⚠️  Failed to extract kubeconform"
      rm -rf "$TMP_DIR"
      echo ""
      echo "    Manual installation options:"
      echo "    1. Visit: https://github.com/yannh/kubeconform/releases"
      echo "    2. Download the ${OS}-${ARCH} release"
      echo "    3. Extract to: $USER_BIN"
      echo "    4. Ensure $USER_BIN is in your PATH"
      exit 1
    fi
  fi
fi

echo ""
echo "✅ Setup complete. Ready to validate K8s YAML."
