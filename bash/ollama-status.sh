#!/usr/bin/env bash
set -u

API_URL="${1:-http://127.0.0.1:11434}"

echo "=== OLLAMA STATUS ==="
echo "API: $API_URL"
echo
if command -v ollama >/dev/null 2>&1; then
  ollama --version
  echo
  ollama list
else
  echo "ollama command not found"
fi
echo
if curl -fsS --max-time 10 "$API_URL/api/tags" >/dev/null; then
  echo "API: reachable"
else
  echo "API: unreachable"
fi
echo
ss -lnt 2>/dev/null | grep ':11434' || echo '11434 not detected'