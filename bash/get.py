import requests

base_url = "http://127.0.0.1:8000"

tasks = requests.get(base_url + "/tasks/all").json()


print(tasks)