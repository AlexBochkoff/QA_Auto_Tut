import os

class Config_Easy:
    """Config class is responsible for storing framework and env configuration 
    Config variables declared:
    1.
    2.
    """
    request_timeout = 10
    user_name = os.environ.get('USERNAME') 
    env = os.environ.get('BQA_ENV')
    os = os.environ.get('OS')
    base_url = 'https://api.github.com/'
    
config = Config_Easy()

# print(config.request_timeout)
# print(config.user_name)
# print(config.env)
# print(config.os)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
