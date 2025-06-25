#!/bin/bash
echo "=== Git Status ==="
git status
echo ""
echo "=== Adding all files ==="
git add .
echo ""
echo "=== Commit ==="
git commit -m "update $(date '+%Y-%m-%d %H:%M:%S')"
echo ""
echo "=== Push to GitHub ==="
git push
echo ""
echo "=== DONE ==="
