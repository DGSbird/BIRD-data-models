import re
import git

# Define the target date
target_date = "2024.01.18"

# Initialize a dictionary to store commit messages
commit_messages = {}

# Initialize a Git repository object
repo = git.Repo()

# Iterate over each commit
for commit in repo.iter_commits():
    # Extract the commit date and message
    commit_date = commit.committed_datetime.strftime("%Y.%m.%d")
    message = commit.message
    
    # Check if the commit date is before the target date
    if commit_date >= target_date:
        # Extract the first occurrence of ">feat:" and prepend the date
        feat_lines = re.findall(r">feat:.*", message)
        if feat_lines:
            # Combine the lines and prepend the date
            # use <br> for line breaks within the markdown table
            feat_message = "<br> ".join(feat_lines) 
            if commit_date in commit_messages:
                commit_messages[commit_date] = commit_messages[commit_date] + "<br> " + feat_message
            else:
                commit_messages[commit_date] = feat_message.strip()  # Remove leading/trailing spaces
            # end if commit_date
        # end if feat_lines
    #end if commit_date >= target_date
# next commit

# Write the markdown table
output_filename = f"git_log_{target_date}.md"
with open(output_filename, "w") as f:
    f.write("| Commit Date | Feature Message |\n")
    f.write("|-------------|-----------------|\n")
    for commit_date, feat_message in commit_messages.items():
        f.write(f"| {commit_date} | {feat_message} |\n")
        f.write("|   |   |\n")
    # next commit_date, feat_message
    f.flush()
    f.close()
# end with

print(f"Markdown table saved to {output_filename}")
