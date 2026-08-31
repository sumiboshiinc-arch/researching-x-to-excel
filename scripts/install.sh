#!/bin/sh
set -eu
repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd -P)
skills_root=${1:-"$HOME/.codex/skills"}
target="$skills_root/researching-x-to-excel"
mkdir -p "$skills_root"

if [ -L "$target" ]; then
  current=$(readlink "$target")
  if [ "$current" = "$repo_root" ]; then
    printf '%s\n' "Already installed: $target -> $repo_root"
    exit 0
  fi
  printf '%s\n' "Refusing to replace symlink: $target -> $current" >&2
  printf '%s\n' "Recovery: move or remove that symlink yourself, then rerun this installer." >&2
  exit 2
fi
if [ -e "$target" ]; then
  printf '%s\n' "Refusing to replace existing path: $target" >&2
  printf '%s\n' "Recovery: move the existing path to a safe backup, then rerun this installer." >&2
  exit 2
fi
ln -s "$repo_root" "$target"
printf '%s\n' "Installed: $target -> $repo_root"
