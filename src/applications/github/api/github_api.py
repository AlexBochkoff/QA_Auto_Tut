import requests

class GitHubAPI:
    """Current class contains every API call we use in tests"""
                      #domain 
    def __init__(self,base_url) -> None:
        self.base_url = base_url

    def get_user(self,username):
        r = requests.get(f"{self.base_url}/users/{username}")
        r.raise_for_status()
        # /\ which means \/
        # if r.status_code != 200:
        #     raise requests.HTTPError

        return r.json()
    
    def get_repos(self,repos_search_param):
        r = requests.get(
            f"{self.base_url}/search/repositories", #?q={repos_search_param}" -- also can be used in url. 
            params={'q' : repos_search_param}
            )
        
        r.raise_for_status()
        
        return r.json()