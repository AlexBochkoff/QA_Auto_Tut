import json
import os
from typing import Any

# First of all, you should add variables to json file, then add them in config class to register, 
# and finally reuse them in our tests or any other places allover the project.


# class DictConfigProvider():

#     def __init__(self, input_values: dict) -> None:
#         super().__init__()
#         self.values = input_values

#     def get(self, item_name: str) -> Any:
#         return self.values[item_name]


class OSConfigProvider(): #Here we declare our provider of OS variables.
    @staticmethod
    def get(item_name: str) -> Any:
        value = os.environ.get(item_name)  # get value from system envs
        return value # return the value


class JSONConfigProvider(): #Here we declare our provider of variables indicated within the json file.
    @staticmethod
    def _read_config(config_path): # parse json file
        with open(config_path) as json_file: # open json file
            return json.load(json_file) # convert to dict/treeMap

    @staticmethod
    def get(item_name: str) -> Any:
        value = JSONConfigProvider._read_config(
            "src\\config\\envs\\dev.json" # Here is the json file adress with the list of variables or constants we want to use further in our tests.
        )  # Read the file
        return value.get(item_name) # get the value from the file by parameter name

# should be done using singleton
class Config: # Here we register our variables provided by the providers above.
    """
    Holds all the settings of your framework
    """

    def __init__(self, config_providers) -> None:
        self.config_providers = config_providers # STORE THE ORDER OF PROVIDERS/SOURCES

        self.conf_dict = {} # STORE OF VALUES OF YOUR PARAMETERS
        
        # BLOCK FOR REGISTERING THE PARAMETERS
        self._register('USERNAME')
        self._register('BQA_ENV')
        self._register('OS')
        self._register('REQUEST_TIMEOUT')
        self._register('BASE_URL')
        # self._register("PARAMETER_ENV")

    # python way
    def __getattr__(self, item_name: str) -> Any: #python
        # config.ITEM_NAME - EXAMPLE OF CALL in PYTHON
        # read about magic methods in python
        if item_name not in self.conf_dict:  # if no value - raise an error
            raise AttributeError(f"Please register '{item_name}' var before usage")

        return self.conf_dict[item_name] # else - return value

    def _register(self, item_name: str) -> None:
        """
        Retieves the value of parameter with item_name name from the 
        config providers/sources and store it in config class for later usage
        """
        for provider in self.config_providers: # iterate over list of config providers/sources
            value = provider.get(item_name) # try to get value by name from config providers/sources
            if value is not None: # if value exists/retrived
                self.conf_dict[item_name] = value # save it to config class
                return # STOP further search

        raise ValueError(f"{item_name} name is missing in config providers")  # if no value for parameter item_name name found - stop TEST FRAMEWORK execution


# dict_confprovider = DictConfigProvider({
#     'BROWSER': 'chrome',
#     'SELENIUM_GRID_URL': 'http://172.19.0.2:4444/wd/hub', # 0.0.0.0 --> selenium-hub
#     })



config = Config([OSConfigProvider, JSONConfigProvider]) # Here we call our config.


# got python - execute from the config file
# print(config.get('PARAMETER_JSON'))
# print(config.get('PARAMETER_ENV'))