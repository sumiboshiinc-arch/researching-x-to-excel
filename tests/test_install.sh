#!/bin/sh
set -eu
repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd -P)
test_root=$(mktemp -d)
trap 'rm -rf "$test_root"' EXIT HUP INT TERM
skills_root="$test_root/skills"
mkdir -p "$skills_root"

"$repo_root/scripts/install.sh" "$skills_root"
test -L "$skills_root/researching-x-to-excel"
test "$(readlink "$skills_root/researching-x-to-excel")" = "$repo_root"

rm "$skills_root/researching-x-to-excel"
mkdir "$skills_root/researching-x-to-excel"
printf '%s\n' unrelated > "$skills_root/researching-x-to-excel/keep.txt"
if "$repo_root/scripts/install.sh" "$skills_root"; then exit 1; fi
test -f "$skills_root/researching-x-to-excel/keep.txt"
