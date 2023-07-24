#!/usr/bin/python3
"""
A Python script that uses REST API, for given set of employers ID,
returns his/her TODO list and exports data in the CSV format and
"""
    

import csv
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

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    filename = idEmp + '.csv'

    with open(filename, "w", newline='') as f:
        write = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in json_req:
            write.writerow([idEmp, usr, i.get('completed'), i.get('title')])
