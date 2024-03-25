#!/usr/bin/python3
"""
    A python script that uses the urlib or request module to fetch data from an API
    """
import requests
import sys

if __name__== "__main__":
    url = "hhtps:jsonplaceholder.typicode.com/users"
    response = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [task.get("title") for task in todos if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(response.get("name"), len(completed), len(todos)))
    [print("\t {}".format(task)) for task in completed]
    