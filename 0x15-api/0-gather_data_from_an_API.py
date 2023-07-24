#!/usr/bin/python3
"""Bash script that uses REST API, for a given employee ID,
and also returns information about his/her TODO list progress."""


import requests as req
import  sys

if __name__ == '__main__':
    url_base = 'https://jsonplaceholder.typicode.com/'
    usr_id = int(sys.argv[1]))
    url = url_base + 'users/' + str(usr_id)
    
    response = req.get(url)
    name = response.json().get('name')

    todo_Url = url + "/todos"
    response = req.get(todo_Url)
    tasks = response.json()
    completed_tasks = []
    completed = 0
    
    
    for task in tasks:
        if task.get('completed') is True:
            completed_tasks.append(task)
            completed += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, len(tasks)))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
