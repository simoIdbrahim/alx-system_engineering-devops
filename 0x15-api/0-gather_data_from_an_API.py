#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress """

import requests
import sys


def gather_data_from_api(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)

    if employee_response.status_code != 200:
        print(f"Error: Unable to fetch data for employee ID {employee_id}")
        sys.exit(1)

    employee_data = employee_response.json()
    employee_name = employee_data.get('name')[:18]

    # Fetch TODO list for the employee
    todo_url = f"{employee_url}/todos"
    todo_response = requests.get(todo_url)

    if todo_response.status_code != 200:
        print(
            f"Error: Unable to fetch TODO list for employee ID {employee_id}")
        sys.exit(1)

    todo_list = todo_response.json()

    # Calculate progress
    total_tasks = len(todo_list)
    completed_tasks = [task for task in todo_list if task.get('completed')]

    # Display results
    print(
        f"Employee {employee_name} is done with tasks("
        f"{len(completed_tasks)}/{total_tasks}):"
    )

    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    gather_data_from_api(employee_id)
