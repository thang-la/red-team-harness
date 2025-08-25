#!/usr/bin/env bash
set -e

echo "=== [SETUP] Environment ==="

# 1) Python venv
if [ ! -d ".venv" ]; then
  echo "[INFO] Creating virtual env..."
  python3 -m venv .venv
fi
source .venv/bin/activate

echo "[INFO] Upgrading pip..."
pip install --upgrade pip

# 2) Install dependencies
echo "[INFO] Installing Python dependencies..."
pip install -r requirements.txt

echo "=== Setup complete ==="
