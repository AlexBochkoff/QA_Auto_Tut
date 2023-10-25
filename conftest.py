import pytest     
# from src.config.config_easy import Config_Easy # Previously it was used here: GitHubAPI(config.BASE_URL)
from src.applications.github.api.github_api import GitHubAPI
from src.config.config_harder import config

@pytest.fixture
def github_api_client(scope = 'session'):
    github_api_client = GitHubAPI(config.BASE_URL)
    yield github_api_client # Yield is generator that allows you to do something after the test. Return doesn't.

    print(' END UP TEST')