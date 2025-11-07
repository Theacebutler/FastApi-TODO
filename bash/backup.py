import requests
import json


def backup():
    base_url = "http://127.0.0.1:8000/tasks/all"
    try:
        tasks = requests.get(base_url)
    except requests.exceptions.ConnectionError:
        print("unable to connct to server, showing the last backup")
        return
    except Exception as e:
        print(e)
        return 
    if tasks.status_code == 200:
        
        with open('data.json', "w") as backup:
            json.dump(tasks.json(), backup)
if __name__ == "__main__":
    backup()