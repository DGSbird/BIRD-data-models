import os
import re
import git
import sqldmlib
import openpyxl

from sqldmlib import entity
from openpyxl import Workbook


# Define the target date
target_date = "2024.01.18"

# instantiate dicts for the changed entity types and their counts.
# Key = entity type name
# Value = count of changes
changed_entity_types = dict()
# Key = entity type name
# Value = created date
changed_entity_types_created_date = dict()
# Key = filename
# Value = count
file_not_found_count = dict()
# Initialize a dictionary to store commit messages
commit_messages = {}

## show progress dot every progress_dot_count times
progress_dot_count = 10


# Initialize a Git repository object
repo = git.Repo(os.getcwd())

# Iterate over each commit
print(f"Finding changes since {target_date}...")
total_changes = int(repo.git.rev_list('--count', '--all', since=target_date))
scanning_text = "Scanning " + str(total_changes) + " commits"
progress_dot_count = int((total_changes / (80 - len(scanning_text))) +1 )
print(f"Scanning {total_changes} commits", end="")
i = 0
for commit in repo.iter_commits():
    i += 1
    if (i / progress_dot_count) == int( i / progress_dot_count):
       print(".", end="", flush=True)

    # Extract the commit date and message
    commit_date = commit.committed_datetime.strftime("%Y.%m.%d")
    message = commit.message
    
    # Check if the commit date is before the target date
    if commit_date >= target_date:
        # Extract the first occurrence of ">feat:" and prepend the date
        feat_lines = re.findall(r">feat:.*", message)
        if feat_lines:
            # # Use this when the message is also to be printed.
            # # Combine the lines and prepend the date
            # feat_message = "<br> ".join(feat_lines) # use <br> for line breaks
            # commit_messages[commit_date] = feat_message.strip()  # Remove leading/trailing spaces

            files = commit.stats.files
            changed_files = [file for file in files if file.startswith('BIRD data models/logical/entity/')]
            for changed_file in changed_files:
                try:
                    entity_type = entity.parse(changed_file, True)
                    name = entity_type.get_name()
                    if name in changed_entity_types:
                        changed_entity_types[name] += 1
                    else:
                        changed_entity_types[name] = 1
                    # end if name
                    created_date = entity_type.get_createdTime()
                    created_date = created_date.get_valueOf_()
                    if name in changed_entity_types_created_date:
                        pass
                    else:
                        changed_entity_types_created_date[name] = created_date
                    # end if name

                except (OSError, FileNotFoundError) :
                    # print (f"File {changed_file} does not exist in commit {commit_hash}")
                    if changed_file in file_not_found_count:
                        file_not_found_count[changed_file] += 1
                    else:
                        file_not_found_count[changed_file] = 1
                # end try
            # next changed_file
        # end if feat_lines
    # end if commit_date
# next commit    
print('.')

# create an excel file to hold the output
work_book  = Workbook()
work_sheet = work_book.active
work_sheet.title = "changed entity types"
work_sheet.append(["Entity type name", "# Changes", "created date"])
# output the file
sorted_entity_types = dict(sorted(changed_entity_types.items()))
output_file = './Changed_Entity_Types'
maxNum = 0
maxName = ''
totalUpdates = 0

# print("===========================================")
# print("list of updated entity types")
# print("===========================================")

for entTp, n in sorted_entity_types.items():
    created_date = changed_entity_types_created_date[entTp]
    created_date_string = f"{created_date}"
    row = [entTp, n, created_date_string]
    work_sheet.append(row)
    if n > maxNum:
        maxNum  = n
        maxName = entTp
    # print(f"{entTp} , {n}")
    totalUpdates = totalUpdates + n
# end for entTp
work_book.save(output_file + '.xlsx')

print()
print("-------------------------------------------")
print(f'Since               : {target_date}')
print(f'Changed entity types: {len(sorted_entity_types)}')
print(f'Total updates       : {totalUpdates}')
print(f'Most updated        : "{maxName}" ({maxNum} times)')
if len(file_not_found_count) == 1:
    print(f'{len(file_not_found_count)} entity has disappeared')
else:
    print(f'{len(file_not_found_count)} entities have disappeared')
print(f'See "{output_file}.xlsx" for more details')
# end if len(file_not_found_count)
