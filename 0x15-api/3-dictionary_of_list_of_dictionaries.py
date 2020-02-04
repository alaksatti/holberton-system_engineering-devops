#!/usr/bin/python3
''' using a specific REST API for a given employee return his todo list '''

if __name__ == '__main__':
    from requests import get
    import json

    employees = get("https://jsonplaceholder.typicode.com/users/").json()

    if employees:
        json_f = {}
        for employee in employees:
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
                                  'completed': task.get('completed'),
                                  'task': task.get('title')})
            json_f[str(employee_id)] = task_list

        with open("todo_all_employees.json", "w") as f:
            json.dump(json_f, f)
