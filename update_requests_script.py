# script to be run inside a gitlab pipline
# checks if there are any open issues from yesterday inside the project with specific labels
# for every found, creates a change request inside the model from info of issue
# if the issue was deleted, delets the respective CRO
import update_requests_from_issues
import sys
import os

# use repo path, cloned each time we run the pipeline
path_of_local_repo = sys.argv[0]
print(path_of_local_repo)
print("Path: ", os.environ['LOCAL_MODEL_PATH'])
# which labels 
list_of_labels = ["New requirement"]
update_requests = update_requests_from_issues.UpdateRequestsFromIssues(os.environ['LOCAL_MODEL_PATH'])
update_requests.update_request_objects(list_of_labels)
print("Finished create request objects process")
