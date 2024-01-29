#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress """

import requests
import sys


if __name__ == '__main__':
    emplId = sys.argv[1]
    palceHolderData = "https://jsonplaceholder.typicode.com/users"
    url = palceHolderData + "/" + emplId

    res = requests.get(url)
    empName = res.json().get('name')

    todoUrl = url + "/todos"
    res = requests.get(todoUrl)
    tasks = res.json()
    done = 0
    taskDone = []

    for task in tasks:
        if task.get('completed'):
            taskDone.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(empName, done, len(tasks)))

    for task in taskDone:
        print("\t {}".format(task.get('title')))
