#!/usr/bin/python3
""" extend your Python script to export data in the JSON format """

import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    res = requests.get(url)
    users = res.json()

    dic = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        res = requests.get(url)
        tasks = res.json()
        dic[user_id] = []
        for task in tasks:
            dic[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })

    with open('todo_all_employees.json', 'w') as file:
        json.dump(dic, file)
