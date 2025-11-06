import requests
from sys import argv


task = argv[1]
des = argv[2]


base_url = "http://127.0.0.1:8000"

post = requests.post(
    url=base_url + '/tasks/add',
    json={
        "title": task,
        "description": des
    }
)
