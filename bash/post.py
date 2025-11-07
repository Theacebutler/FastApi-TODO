from requests import post
from requests.exceptions import ConnectionError
import json
from sys import argv
from utils import get_config
from backup import save_upload

task = argv[1]
des = argv[2]

base_url = get_config("base_url")
data ={
        "title": task,
        "description": des
    }
tasks = json.dumps(data)
try:
    # delete the pending tasks
    with open("backups/upload.json", "w") as upload:
        upload.write("")

    request = post(
        url=base_url + '/add',
        data=tasks
    )
except ConnectionError:
    print("Conntion error, saveing file to local backup...")
    save_upload(tasks)
except Exception as e:
    print(e)
    save_upload(tasks) 