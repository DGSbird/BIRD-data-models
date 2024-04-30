#!/bin/bash

# Script that lists all branches that have local commits that have not
# been pushed to remote.

# Get the list of local branches
branches_output=$(git branch)
branches=($(echo "$branches_output" | tr -d '*' | awk '{$1=$1};1'))  # Remove the "*" and leading/trailing spaces

# Initialize a list to store unpushed branches
unpushed_branches=()

# Check each branch for unpushed commits
for branch in "${branches[@]}"; do
    branch_name=$(echo "$branch" | xargs)  # Remove any extra spaces
    # Check if the branch has unpushed commits
    if ! git rev-list --left-right "origin/$branch_name...$branch_name" &> /dev/null; then
        # If an error occurs, the branch has unpushed commits
        unpushed_branches+=("$branch_name")
    fi
done

# Print the unpushed branches
if [ ${#unpushed_branches[@]} -gt 0 ]; then
    echo "Local branches with unpushed commits:"
    for branch in "${unpushed_branches[@]}"; do
        echo "- $branch"
    done
else
    echo "All local branches have been pushed to remote."
fi
