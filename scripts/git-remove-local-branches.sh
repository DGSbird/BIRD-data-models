#!/bin/sh

# Script to remove the branches that exists locally, but do not exist
# remotely.
# The script will first list the local branches and then ask for
# confirmation before deleting the branches.
# Run this script from the git bash command line.

# This command consists of several parts:

# git fetch -p: This command ensures that the remote branches are up-to-date.
# git for-each-ref --format '%(refname:short) %(upstream:track)': This command returns the Git branches in a format of our choosing, where we have both the local branch name as well as the upstream branch (which will be “[gone]” for branches where the remote was deleted).
# awk '$2 == "[gone]" {print $1}': This command filters the branches which remote status is “[gone]” and returns the local branch name.
# xargs -r git branch -D: This command deletes the local branch.

git fetch -p && git for-each-ref --format '%(refname:short) %(upstream:track)' | awk '$2 == "[gone]" {print $1}' > branches.txt
echo "The following branches will be deleted:"
cat branches.txt
read -p "Are you sure? (y/n) " answer
if [ "$answer" = "y" ]; then
  xargs -r git branch -D < branches.txt
  echo "Deleted."
else
  echo "Canceled."
fi
rm branches.txt
