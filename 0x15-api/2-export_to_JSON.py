#!/usr/bin/python3
''' using a specific REST API for a given employee return his todo list '''


def employee_info(uid):
    ''' retrieve employee info '''
    employee = get("https://jsonplaceholder.typicode.com/users/" + uid).json()

    if employee:
        employee_id = employee.get('id')
        employee_username = employee.get('username')
        tasks = get('https://jsonplaceholder.typicode.com/todos/').json()
        wanted_tasks = []

        for task in tasks:
            if task['userId'] == employee_id:
                wanted_tasks.append(task)
        task_list = []
        for task in wanted_tasks:
            task_list.append({'username': employee_username,
                              'name': employee_username,
                              'completed': task.get('completed'),
                              'title': task.get('title')})

        json_f = {str(employee_id): task_list}

        with open("{}.json".format(employee_id), "w") as f:
            json.dump(json_f, f)

if __name__ == '__main__':
    from requests import get
    from sys import argv
    import json

    if len(argv) == 2 and argv[1].isdigit():
        employee_info(argv[1])
