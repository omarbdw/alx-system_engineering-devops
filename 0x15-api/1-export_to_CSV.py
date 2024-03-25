#!/usr/bin/python3
"""Gather data from an API and export to CSV"""

import csv
import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    employee = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(userId),
        timeout=5)

    employeeName = employee.json().get('name')

    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos', timeout=5)
    TOTAL = 0
    DONE = 0

    tasks = []
    for task in todos.json():
        if task.get('userId') == int(userId):
            TOTAL += 1
            if task.get('completed'):
                DONE += 1
            tasks.append(task)

    # Export data to CSV
    filename = "{}.csv".format(userId)
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL, delimiter=',',
                            quotechar='"', lineterminator='\n')

        for task in tasks:
            writer.writerow([userId, employeeName, task.get('completed'),
                             task.get('title')])
