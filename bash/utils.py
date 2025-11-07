import json


with open("config.json", "r") as config:
    all_configs =  json.load(config)


    
def get_config(config: str):
    return all_configs[0][f"{config}"]


def set_config(key: str, value: str):
    with open("config.json", "w") as config:
        
        pass