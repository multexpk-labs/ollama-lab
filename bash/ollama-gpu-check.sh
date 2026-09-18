#!/usr/bin/env bash
set -u

echo "=== OLLAMA GPU CHECK ==="
if command -v nvidia-smi >/dev/null 2>&1; then
  nvidia-smi --query-gpu=name,memory.total,memory.used,memory.free,utilization.gpu --format=csv
else
  echo "nvidia-smi not available"
fi