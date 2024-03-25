#!/usr/bin/python3
"""Gather data from an API and export to JSON"""
import json
import requests
import sys


if __name__ == "__main__":
    # Get all employees
    employees = requests.get(
        'https://jsonplaceholder.typicode.com/users', timeout=5)
    employees = employees.json()

    # Get all todos
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos', timeout=5)
    todos = todos.json()

    # Create a dictionary of all employees and their tasks
    data = {}
    for employee in employees:
        userId = employee.get('id')
        employeeName = employee.get('username')
        user_tasks = []
        for task in todos:
            if task.get('userId') == userId:
                task_data = {
                    "username": employeeName,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                user_tasks.append(task_data)
        data[userId] = user_tasks

    # Save data to JSON file
    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
