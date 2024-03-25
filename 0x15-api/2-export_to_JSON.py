#!/usr/bin/python3
"""Gather data from an API and export to CSV"""

import json
import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    employee = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(userId),
        timeout=5)

    employeeName = employee.json().get('username')

    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos', timeout=5)

    # Export data to JSON
    filename = "{}.json".format(userId)

    tasks = todos.json()
    user_tasks = []
    for task in tasks:
        if task.get('userId') == int(userId):
            task_data = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": employeeName
            }
            user_tasks.append(task_data)

    data = {userId: user_tasks}

    with open(filename, 'w') as file:
        json.dump(data, file)
