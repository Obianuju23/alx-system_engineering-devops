#!/usr/bin/python3
"""Bash script that uses REST API, for a given employee ID,
and also returns information about his/her TODO list progress."""


import requests as req
import  sys

if __name__ == '__main__':
    uid = int(sys.argv[1])
    baseUrl = "https://jsonplaceholder.typicode.com/"
    url = baseUrl + "users/" + str(uid)

    response = rq.get(url)
    name = response.json().get('name')

    todoUrl = url + "/todos"
    response = rq.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed') is True:
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
