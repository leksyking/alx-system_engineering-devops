#!/usr/bin/python3
"""
    Making requests to a REST API for todo lists of employees' progress
"""

import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = r.get(url + 'users/{}'.format(sys.argv[1])).json()
    todo = r.get(url + 'todos', params={'userId': sys.argv[1]}).json()

    completed = [title.get("title") for title in todo if
                 title.get('completed') is True]
    print(completed)
    print("Employee {} is done with tasks({}/{}):".format(user_id.get("name"),
                                                          len(completed),
                                                          len(todo)))
    [print("\t {}".format(title)) for title in completed]
