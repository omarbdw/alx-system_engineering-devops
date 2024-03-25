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
    data = {}
    for user in todos.json():
        userId = user.get('userId')
        task = {
            "username": employeeName,
            "task": user.get('title'),
            "completed": user.get('completed')
        }
        if userId in data:
            data[userId].append(task)
        else:
            data[userId] = [task]

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
