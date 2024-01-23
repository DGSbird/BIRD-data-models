#!/bin/bash

######
# Date: 2023-11-20
# Author: A.J. Bos
# Description: 
# Script to find all entity types that are listed in the file
# structure of the model, but that are not part of the logical design
# file. This is a mistake and should be rectified by hand.
#
# For more background see gitlab issue 415
# (https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/415)
# how to resolve 
#
# Run it from the git bash prompt.
# Run this file from the root of the git repo, so where the .git and
# .gitlab directories are located.
####


# Set the directory path to the location of the files that represent
# the entity types.
dir="./BIRD data models/logical/entity/"

# Find all files in the directory and remove the .xml file extension.
names=$(find "$dir" -type f -printf "%f\n" | sed 's/\.xml$//')

# Extract the values of the 'oid' attributes from the specified file
# that contains the logical design of the complete LDM.
compare=$(grep -oP '(?<=oid=")[^"]*' "$dir/../subviews/9D13FB9C-8E29-8E21-0CDD-BB4AE72F38F5.xml")

# Compare the two lists of file names and output the differences.
diff=$(comm -23 <(echo "$names" | sort) <(echo "$compare" | sort))
echo "The following files do not match the values of the 'oid' attributes in '9D13FB9C-8E29-8E21-0CDD-BB4AE72F38F5.xml':"
echo "$diff"
