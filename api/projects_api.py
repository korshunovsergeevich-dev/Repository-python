import requests


class ProjectsApi:
    BASE_URL = "https://yougile.com/api-v2"

    def __init__(self, token):
        self.session = requests.Session()

        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def create_project(self, title):

        response = self.session.post(
            f"{self.BASE_URL}/projects",
            json={
                "title": title
            }
        )

        return response

    def update_project(self, project_id, title):

        response = self.session.put(
            f"{self.BASE_URL}/projects/{project_id}",
            json={
                "title": title
            }
        )

        return response

    def get_project(self, project_id):

        response = self.session.get(
            f"{self.BASE_URL}/projects/{project_id}"
        )

        return response
