#!/bin/bash
# Skills Hub Sync & Validation Script
#
# Usage:
#   ./scripts/sync.sh              # Full sync + validate
#   ./scripts/sync.sh --validate   # Validate only
#   ./scripts/sync.sh --sync       # Sync plugin.json only
#   ./scripts/sync.sh --check-tests # Check tests only

cd "$(dirname "$0")/.." || exit 1

echo "🔄 Skills Hub Sync & Validation"
echo "================================"

# Check if Python is available
if command -v python3 &> /dev/null; then
    python3 scripts/sync.py "$@"
elif command -v python &> /dev/null; then
    python scripts/sync.py "$@"
else
    echo "❌ Python not found. Please install Python 3."
    exit 1
fi