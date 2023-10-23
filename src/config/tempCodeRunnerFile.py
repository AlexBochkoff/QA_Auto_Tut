class JSONConfigProvider():
    @staticmethod
    def _read_config(config_path): # parse json file
        with open(config_path) as json_file: # open json file
            return json.load(json_file) # convert to dict/treeMap

    @staticmethod
    def get(item_name: str) -> Any:
        value = JSONConfigProvider._read_config(
            ".\\config\\envs\\dev.json"
        )  # Read the file
        return value.get(item_name) # get the value from the file by parameter name