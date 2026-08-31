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
"$repo_root/scripts/install.sh" "$skills_root" | grep -q 'Already installed:'

rm "$skills_root/researching-x-to-excel"
printf '%s\n' unrelated > "$skills_root/researching-x-to-excel"
if "$repo_root/scripts/install.sh" "$skills_root" 2>"$test_root/file.err"; then exit 1; fi
grep -q 'Recovery:' "$test_root/file.err"
test -f "$skills_root/researching-x-to-excel"
rm "$skills_root/researching-x-to-excel"
ln -s /tmp/unrelated-skill "$skills_root/researching-x-to-excel"
if "$repo_root/scripts/install.sh" "$skills_root" 2>"$test_root/link.err"; then exit 1; fi
grep -q 'Recovery:' "$test_root/link.err"
test "$(readlink "$skills_root/researching-x-to-excel")" = /tmp/unrelated-skill
