#!/usr/bin/python3
"""Shebang"""
import requests
from sys import argv
import csv


def get_info():
    """Gets data from restAPI"""
    user_id = int(argv[1])
    users_json = (requests.get('https://jsonplaceholder.typicode.com/users/{}'
                               .format(user_id))).json()
    todos_json = (requests.get('https://jsonplaceholder.typicode.com/\
todos?userId={}'.format(user_id))).json()
    t_list = []
    for t in todos_json:
        t_list.append([user_id, users_json["name"], t['completed'],
                       t['title']])
    with open("{}.csv".format(user_id), "w") as fd:
        writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
        writer.writerows(t_list)


if __name__ == '__main__':
    get_info()
