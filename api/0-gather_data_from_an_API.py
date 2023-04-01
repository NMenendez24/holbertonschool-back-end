#!/usr/bin/python3

import requests
from sys import argv


def get_info():
    """Gets data from restAPI"""
    user_id = int(argv[1])
    users_json = (requests.get('https://jsonplaceholder.typicode.com/users/{}'
                               .format(user_id))).json()
    todos_json = (requests.get('https://jsonplaceholder.typicode.com/\
todos?userId={}'.format(user_id))).json()
    completed_tasks, tasks, task_list = 0, 0, []
    for t in todos_json:
        if t['completed'] is True:
            completed_tasks += 1
            task_list.append("\t {}".format(t['title']))
        tasks += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(users_json['name'], completed_tasks, tasks))
    print(*task_list, sep='\n')


if __name__ == '__main__':
    get_info()
