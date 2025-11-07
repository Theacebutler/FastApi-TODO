import requests
from requests.exceptions import ConnectionError
from sys import argv
from datetime import datetime
from utils import get_config
from backup import read_backup, backup
base_url = get_config("base_url")
completed = ""

try:
    tasks = requests.get(base_url + f"/all").json()
except ConnectionError:
    print("Unable to connct, getting data from local backup...")
    tasks = read_backup()
timestamp = str(tasks[0]['created_at'][:10])+ ' ' + str(tasks[0]['created_at'][11:-7])
for task in tasks:
    date = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    print(f"{date} | task id: {task['id']} | Title: {task['title']} | Description: {task['description']}\n")
backup(tasks)