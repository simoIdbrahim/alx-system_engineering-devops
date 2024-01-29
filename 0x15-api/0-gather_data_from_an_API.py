#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress """

import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch user details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch user's TODO list
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    done_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Display information
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")

    # Display completed tasks
    for todo in todos_data:
        if todo['completed']:
            print(f"\t {todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
