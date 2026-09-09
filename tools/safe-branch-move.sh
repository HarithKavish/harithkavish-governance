#!/usr/bin/env bash
# safe-branch-move.sh <target-ref> [--force]
#
# Refuses to move the current branch's tip (reset --hard, or any equivalent that
# would discard commits) when doing so would drop commits an OPEN pull request
# depends on. Run from inside the repo, on the branch being moved.
#
# ROOT CAUSE this exists for (not the symptom that first revealed it):
# a persistent contributor branch (feature/claude) got hard-reset to a stale
# target while it was the head of an open, unmerged PR, silently discarding a
# commit that PR depended on. Recovered via reflog+cherry-pick, but only found
# because a diff was checked by chance afterward. This script makes that check
# structural instead of remembered -- it runs before the move, not after.
#
# Usage:
#   safe-branch-move.sh origin/development          # check, then move if safe
#   safe-branch-move.sh origin/development --force   # move regardless, loudly

set -euo pipefail

TARGET="${1:?usage: safe-branch-move.sh <target-ref> [--force]}"
FORCE="${2:-}"

CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
CURRENT_SHA="$(git rev-parse HEAD)"
TARGET_SHA="$(git rev-parse "$TARGET")"

if [ "$CURRENT_SHA" = "$TARGET_SHA" ]; then
  echo "safe-branch-move: already at $TARGET ($TARGET_SHA), nothing to do."
  exit 0
fi

# Does any OPEN PR use this branch as its head?
REPO_SLUG="$(gh repo view --json nameWithOwner --jq .nameWithOwner 2>/dev/null || echo '')"
if [ -z "$REPO_SLUG" ]; then
  echo "safe-branch-move: could not determine repo (not a GitHub repo, or gh not authed)." >&2
  echo "safe-branch-move: refusing to guess. Pass --force to move anyway." >&2
  [ "$FORCE" = "--force" ] || exit 2
fi

OPEN_PRS=""
if [ -n "$REPO_SLUG" ]; then
  OPEN_PRS="$(gh pr list --repo "$REPO_SLUG" --head "$CURRENT_BRANCH" --state open --json number,baseRefName --jq '.[] | "\(.number)\t\(.baseRefName)"' 2>/dev/null || echo '')"
fi

if [ -z "$OPEN_PRS" ]; then
  echo "safe-branch-move: no open PR has $CURRENT_BRANCH as its head. Safe to move."
  git reset --hard "$TARGET_SHA"
  echo "safe-branch-move: $CURRENT_BRANCH -> $TARGET_SHA"
  exit 0
fi

# An open PR depends on this branch. Would the move lose commits it needs?
UNIQUE_COMMITS="$(git log --oneline "$TARGET_SHA".."$CURRENT_SHA" 2>/dev/null || echo '')"

if [ -z "$UNIQUE_COMMITS" ]; then
  echo "safe-branch-move: $CURRENT_BRANCH has open PR(s) below, but no commits unique"
  echo "safe-branch-move: to it relative to $TARGET -- nothing would be lost."
  echo "$OPEN_PRS" | while IFS=$'\t' read -r num base; do echo "  PR #$num -> $base"; done
  git reset --hard "$TARGET_SHA"
  echo "safe-branch-move: $CURRENT_BRANCH -> $TARGET_SHA"
  exit 0
fi

echo "safe-branch-move: REFUSING." >&2
echo "safe-branch-move: $CURRENT_BRANCH is the head of an open pull request:" >&2
echo "$OPEN_PRS" | while IFS=$'\t' read -r num base; do echo "  PR #$num -> $base" >&2; done
echo "safe-branch-move: and moving to $TARGET would discard these unique commits:" >&2
echo "$UNIQUE_COMMITS" | sed 's/^/  /' >&2
echo "safe-branch-move: merge or close that PR first, or verify these commits are" >&2
echo "safe-branch-move: already reflected in $TARGET by content (not just assumed)," >&2
echo "safe-branch-move: then re-run with --force." >&2

if [ "$FORCE" = "--force" ]; then
  echo "safe-branch-move: --force given. Moving anyway." >&2
  git reset --hard "$TARGET_SHA"
  echo "safe-branch-move: $CURRENT_BRANCH -> $TARGET_SHA (forced)"
  exit 0
fi

exit 1
