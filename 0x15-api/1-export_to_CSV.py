#!/usr/bin/python3
"""Python script that, using this REST API, for
a given employee ID, returns information about
 his/her TO list progress.
 and export into csv"""
import csv
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    # *get todo where userID = id
    todos = requests.get(url + "todos", {"userId": id}).json()

    name = user.get("username")

    file_name = "{}.csv".format(id)
    with open(file_name, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for item in todos:
            completed_status = item.get("completed")
            task_title = item.get("title")

            writer.writerow([id, name, completed_status, task_title])
