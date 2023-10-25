def __getattr__(self, item_name: str) -> Any: #python
        # config.ITEM_NAME - EXAMPLE OF CALL in PYTHON
        # read about magic methods in python
        print(item_name)
        if item_name not in self.conf_dict:  # if no value - raise an error
            raise AttributeError(f"Please register '{item_name}' var before usage")