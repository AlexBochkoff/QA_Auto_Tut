# Execute the command pytest( .) or python3 -m pytest to start testing

from src.config.config_easy import Config_Easy
# from src.config.config_harder import config

def test_api_lists():
    assert [1, 2, 3] == [1, 2, 3] # Comparison between lists
    # identical to:
    # if [1, 2, 3] != [1, 2, 3]:
    #     raise AssertionError("Not equal")

def test_api_request_timeout():
    print(Config_Easy.request_timeout)
    # print(config.BASE_URL_UI)

def test_api_user_name():
    print(Config_Easy.user_name)

def test_api_env():
    print(Config_Easy.env)

def test_api_os():
    print(Config_Easy.os)