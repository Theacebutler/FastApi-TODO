import requests
from sys import argv
from datetime import datetime
base_url = "http://127.0.0.1:8000"
completed = ""
if "-o" in argv:
    completed = "open"
tasks = requests.get(base_url + f"/tasks/all/{completed}").json()
x = str(tasks[0]['created_at'][:10])+ ' ' + str(tasks[0]['created_at'][11:-7])
for task in tasks:
    date = datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
    print(f"{date} | task id: {task['id']} | Title: {task['title']} | Description: {task['description']}\n")
