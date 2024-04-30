# script to be run inside a gitlab pipline
# checks if there are any pushed changes which are not connected to a change request object
import check_pushed_changes
import sys
import os

# use repo path, cloned each time we run the pipeline
path_of_local_repo = sys.argv[0]
print(path_of_local_repo)
print("Path: ", os.environ['LOCAL_MODEL_PATH'])
check = check_pushed_changes.CheckPushedChanges()
check.check_latest_changes()
print("Finished checking changes process")