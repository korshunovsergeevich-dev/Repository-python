import os
import pytest
from dotenv import load_dotenv
from api.projects_api import ProjectsApi


load_dotenv()


@pytest.fixture(scope="session")
def api_token():
    token = os.getenv("YOUGILE_TOKEN")

    return token


@pytest.fixture
def project_api(api_token):
    return ProjectsApi(api_token)
