import json


def read_backup():
    # read the local backup file
    with open('backups/backup.json', 'r') as backup:
        tasks = json.load(backup)
    return tasks


def backup(data):
    # save fetched tasks to local storage
    with open('backups/backup.json', 'w')as backup:
        json.dump(data, backup)


def save_upload(task):
    # save unuploaded tasks
    with open('backups/upload.json', 'w') as local:
        json.dump(task, local)

def read_upload():
    # read changes that didnt upload
    with open('backups/upload.json', 'r') as local:
        local_upload = json.load(local)
        return local_upload