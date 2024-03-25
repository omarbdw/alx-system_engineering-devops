#!/usr/bin/python3
"""Gather data from an API"""

import sys
import requests

if __name__ == "__main__":

    userId = int(sys.argv[1])
    employee = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(userId),
        timeout=5)
    employeeName = employee.json().get('name')

    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos', timeout=5)
    TOTAL = 0
    DONE = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            TOTAL += 1
            if task.get('completed'):
                DONE += 1

    print('Employee {} is DONE with tasks({}/{}):'
          .format(employeeName, DONE, TOTAL))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
