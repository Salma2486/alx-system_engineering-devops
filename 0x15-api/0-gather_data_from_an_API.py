#!/usr/bin/python3
""" teiortg jmoe5ym gikhwsytrg"""

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    completed = [task.get("title") for task in todos if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    [print("\t {}".format(complete)) for complete in completed]
