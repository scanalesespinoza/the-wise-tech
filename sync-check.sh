#!/usr/bin/env bash
set -euo pipefail

UPSTREAM_REMOTE="${UPSTREAM_REMOTE:-upstream}"
UPSTREAM_URL="${UPSTREAM_URL:-https://github.com/scanalesespinoza/the-wise-tech.git}"
DEFAULT_BRANCH="${DEFAULT_BRANCH:-main}"

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "This script must be executed inside a git repository." >&2
  exit 1
fi

if ! git remote | grep -qx "$UPSTREAM_REMOTE"; then
  git remote add "$UPSTREAM_REMOTE" "$UPSTREAM_URL"
  echo "Added remote '$UPSTREAM_REMOTE' → $UPSTREAM_URL"
else
  current_url=$(git remote get-url "$UPSTREAM_REMOTE")
  if [ "$current_url" != "$UPSTREAM_URL" ]; then
    git remote set-url "$UPSTREAM_REMOTE" "$UPSTREAM_URL"
    echo "Updated remote '$UPSTREAM_REMOTE' to $UPSTREAM_URL"
  fi
fi

echo "Fetching latest refs from $UPSTREAM_REMOTE…"
git fetch "$UPSTREAM_REMOTE" --tags --prune >/dev/null

if git show-ref --verify --quiet "refs/heads/$DEFAULT_BRANCH"; then
  LOCAL_REF="refs/heads/$DEFAULT_BRANCH"
else
  LOCAL_REF=$(git symbolic-ref --quiet --short HEAD || echo "HEAD")
fi

UPSTREAM_REF="refs/remotes/$UPSTREAM_REMOTE/$DEFAULT_BRANCH"

if ! git show-ref --verify --quiet "$UPSTREAM_REF"; then
  echo "Upstream branch '$UPSTREAM_REMOTE/$DEFAULT_BRANCH' not found. Verify DEFAULT_BRANCH." >&2
  exit 1
fi

LOCAL_HEAD=$(git rev-parse "$LOCAL_REF")
UPSTREAM_HEAD=$(git rev-parse "$UPSTREAM_REF")
MERGE_BASE=$(git merge-base "$LOCAL_HEAD" "$UPSTREAM_HEAD")

if [ "$UPSTREAM_HEAD" = "$LOCAL_HEAD" ]; then
  echo "✅ Already in sync with $UPSTREAM_REMOTE/$DEFAULT_BRANCH"
  exit 0
fi

echo "🔍 Upstream contains new commits."
echo "Last sync point (merge-base): $MERGE_BASE"
echo "Local head:    $LOCAL_HEAD"
echo "Upstream head: $UPSTREAM_HEAD"

echo "\nFiles changed upstream since the last sync point:"
if git diff --name-status "$MERGE_BASE" "$UPSTREAM_HEAD"; then
  echo "\nReview the changes above and merge or cherry-pick as needed."
else
  echo "(No file-level differences detected — check commit history manually.)"
fi

echo "\n💡 Suggestion: Create a new branch, pull from '$UPSTREAM_REMOTE/$DEFAULT_BRANCH', and open a Pull Request to integrate these improvements."
