import gitlab
import os
import logging

TEAM_GROUP_NAME = "SDD-BIRD-Team"
PROJECT_NAME = "bird-logical-data-model"

class CheckPushedChanges:
    """Checks if there all objects that were pushed as a change have a change request objects also added.
    """
    def __init__(self) -> None:
        self.gl_client = gitlab.Gitlab(url='https://gitlab.sofa.dev', private_token=os.environ['GITLAB_API_TOKEN'])

    def check_latest_changes(self):
        """Prints a warning if there are any changes in the last commit that are not connected to a change request
        """
        sdd_bird_team = self.gl_client.groups.get(TEAM_GROUP_NAME)
        groups_projects = sdd_bird_team.projects.list(all=True)
        for project in groups_projects:
            if project.name == PROJECT_NAME:
                group_project = project
        gp_id = group_project.id
        project = self.gl_client.projects.get(gp_id)
        newest_commit = project.commits.list(ref_name='develop', all=False)[0]
        for diff in newest_commit.diff():
            if (
                not diff["deleted_file"]
                and "\n+<requestID>" not in diff["diff"]
                and (
                    "entity" in diff["new_path"]
                    or "rel" in diff["new_path"]
                    or "inheritance" in diff["new_path"]
                )
            ):
                new_path = diff["new_path"]
                logging.warning(f"Change of file {new_path} is not connected to a change request object.")