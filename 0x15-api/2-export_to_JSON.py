#!/usr/bin/python3
"""
A Python sript that uses a REST API, for a given employee ID,
returns his/her TODO list progress and exports data in JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = []
    Json_data = {}

    for all_Emp in json_req:
        totalTasks.append(
            {
                "task": all_Emp.get('title'),
                "completed": all_Emp.get('completed'),
                "username": usr,
            })
    Json_data[idEmp] = totalTasks

    Json_file = idEmp + ".json"
    with open(Json_file, 'w') as f:
        json.dump(Json_data, f)
