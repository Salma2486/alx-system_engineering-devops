#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to a CSV file.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then writes the tasks to a CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get the employee information using the provided employee ID
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Get the to-do list for the employee using the provided employee ID
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params=params).json()

    # Prepare data for CSV
    data = [[t.get("userId"), user.get("name"), t.get("completed"), t.get("title")] for t in todos]

    # Write data to CSV
    with open('{}.csv'.format(employee_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
