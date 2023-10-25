# Execute the command pytest( .) -v -s(view all tests with statuses) or python3 -m pytest -v -s to start testing
import requests
import pytest
# from src.config.config_easy import Config_Easy # 1.
from src.config.config_harder import config
# from src.applications.github.api.github_api import GitHubAPI # 2. As soon as ## 1 and 2 are called in conftest.py we can delete them here. 

def test_api_request_timeout():
    print(config.REQUEST_TIMEOUT)
    # print(config.BASE_URL_UI)

def test_api_user_name():
    print(config.USERNAME)

def test_api_env():
    print(config.BQA_ENV)

def test_api_os():
    print(config.OS)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def test_api_lists():
    assert [1, 2, 3] == [1, 2, 3] # Comparison between lists
    # or:
    # if [1, 2, 3] != [3, 2, 1]:
    #     raise AssertionError("Not equal")

def test_http_status_code_200():
    r = requests.get('https://api.github.com/zen')
    # print(r.__dict__)# Used to see more details
    assert r.status_code == 200
    #assert r.text != 'Speak like a human.'# -- This is a flacky test. If you work on your PC its ok. Else, if it's not, it can fail from time to time. It's better to delete it.

def test_user_exists(github_api_client):
    #r = requests.get('https://api.github.com/users/defunct')
    # print(r.__dict__)
    # assert r.json()['login'] == 'defunct'
    # assert r.json()['id'] == 371421
    
    # The same as /\ but we use class from applications.api.github_api
    #github_api_client = GitHubAPI(Config_Easy.base_url) # Base_url itself can be put here instead.
    user = github_api_client.get_user('defunct')
    assert user['login'] == 'defunct'
    assert user['id'] == 371421

def test_user_not_exist(github_api_client): # We now reuse fixture from conftest.py here.
    # r = requests.get('https://api.github.com/users/asdgas97a9sdgas9as2')
    # print(r.__dict__)
    # assert r.status_code == 404
    # assert r.json()['message'] == 'Not Found'

    # The same as /\ but we use class from applications.api.github_api
    #github_api_client = GitHubAPI('https://api.github.com/')
    with pytest.raises(requests.exceptions.HTTPError):
        github_api_client.get_user('asdgas97a9sdgas9as2')
    
    # assert r.status_code == 404
    # assert user['message'] == 'Not Found'

def test_check_repos_can_be_found(github_api_client): # Check that user can find any existing repo from github.
    repos = github_api_client.get_repos('qa_auto_tut')

    assert repos['total_count'] != 0
    assert len(repos['items']) != 0

def test_check_repos_cannot_be_found(github_api_client): # Check that user can find any existing repo from github.
    repos = github_api_client.get_repos('89a7sd56gasd')

    #print(repos) -- Used here for debugging only. Should be deleted after checkout. 

    assert repos['total_count'] == 0
    assert len(repos['items']) == 0