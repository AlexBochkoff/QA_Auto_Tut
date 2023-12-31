import requests

class GitHubAPI: # Here we declare all the api methods we use in tests.
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
            f"{self.base_url}/search/repositories", #?q={repos_search_param}" -- also can be used in url here. 
            params={'q' : repos_search_param}
            )
        # print(f"Response retriewed {r}")  # For validation that we get the info needed we can use this simple print to see the body of the response.
        
        r.raise_for_status()
                
        return r.json()