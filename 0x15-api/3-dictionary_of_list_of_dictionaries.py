#!/usr/bin/python3
"""
    Export data in JSON format
"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    dictionary = {}
    for user in users:
        user_Id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_Id)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dictionary[user_Id] = []
        for task in tasks:
            dictionary[user_Id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
        