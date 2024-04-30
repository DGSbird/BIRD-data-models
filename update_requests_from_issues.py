import gitlab
from sqldmlib import model_service

import os
from datetime import datetime, timedelta

TEAM_GROUP_NAME = "SDD-BIRD-Team"
PROJECT_NAME = "bird-logical-data-model"

class UpdateRequestsFromIssues:
    """Checks if there is any new issue created (open + specific label) and creates a request object from that issue.
    When a request object is created, issue is set to closed.
    """
    def __init__(self, path: str) -> None:
        self.gl_client = gitlab.Gitlab(url='https://gitlab.sofa.dev', private_token=os.environ['GITLAB_API_TOKEN'])
        self.path = path

    def get_yesterday_issues(self, labels: list=[]):
        """Uses gitlab api to find open issues of this project
        """
        sdd_bird_team = self.gl_client.groups.get(TEAM_GROUP_NAME)
        groups_projects = sdd_bird_team.projects.list(all=True)
        for project in groups_projects:
            if project.name == PROJECT_NAME:
                group_project = project
        gp_id = group_project.id
        project = self.gl_client.projects.get(gp_id)
        open_issues = project.issues.list(state="opened", all=True)
        # filter issues that were opened yesterday
        issues_opened_yesterday = self.issues_opened_or_updated_yesterday(open_issues)
        # if classification by labels needed replace the return with the following
        # project.issues.list(labels=labels, state="opened")
        return issues_opened_yesterday

    def get_all_issues(self):
        """Uses gitlab api to find issues of this project
        """
        sdd_bird_team = self.gl_client.groups.get(TEAM_GROUP_NAME)
        groups_projects = sdd_bird_team.projects.list(all=True)
        for project in groups_projects:
            if project.name == PROJECT_NAME:
                group_project = project
        gp_id = group_project.id
        project = self.gl_client.projects.get(gp_id)
        return project.issues

    def issues_opened_or_updated_yesterday(self, open_issues: list):
        """Uses gitlab api to find issues of this project that were opened or updated yesterday
        """
        issues_opened_yesterday = []
        today = datetime.today()
        yesterday = today - timedelta(days=1)
        yesterday = yesterday.date()
        for issue in open_issues:
            updated_at = issue.updated_at
            updated_at = updated_at.split("T")[0]
            py_updated_at = datetime.strptime(updated_at, "%Y-%m-%d").date()
            if yesterday == py_updated_at:
                issues_opened_yesterday.append(issue)
        return issues_opened_yesterday

    def update_request_objects(self, labels:list=[]):
        sql_dm_service = model_service.SqlDataModelerService(self.path)
        # import model content
        sql_dm_service.import_sql_objects(self.path)
        # check if there are new open issues with specific label
        open_issues = self.get_yesterday_issues(labels)
        all_issues = self.get_all_issues()
        # for every new issue create a request object
        #     1. GI.label = Status::open => CRO.status = proposed, 
        #     2. GI.label = Status::in progress => CRO.status = implementing, 
        #     3. GI.label = Status::done => CRO.status = implemented
        for open_issue in open_issues:
            # author = open_issue.author['name']
            # created_at = open_issue.created_at
            description = open_issue.description
            title = open_issue.title
            url = open_issue.web_url
            labels = open_issue.labels
            status = ""
            if "Status::open" in labels:
                status = "proposed"
            elif "Status::in progress" in labels:
                status = "implementing"
            elif "Status::done" in labels:
                status = "implemented"
            # TODO: maybe add info on author
            id_from_issue = f"{open_issue.id}-{open_issue.iid}" 
            sql_dm_service.add_sql_change_request_to_model(self.path, title, comment=description, notes=url, id=id_from_issue, status=status)
        # go through cros and check if for each the realated issue exists
        # if not, it was deleted
        cros = sql_dm_service._sql_change_request_service._sql_change_requests_by_id
        for cro in cros:
            issue_iid = cro.split("-")[1]
            try:
                all_issues.get(issue_iid)
            except:
                print("Issue with iid ", issue_iid, " was deleted.")
                print("Deleting CRO ", cro)
                sql_dm_service.remove_sql_change_request_object(cro)
        return True       
