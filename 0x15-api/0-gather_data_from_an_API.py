#!/usr/bin/python3
''' using a specific REST API for a given employee return his todo list '''


def employee_info(uid):
    ''' retrieve employee info '''
    employee = get("https://jsonplaceholder.typicode.com/users/" + uid).json()

    if employee:
        t = get('https://jsonplaceholder.typicode.com/todos?userId=' + uid)
        tasks = t.json()
        task_total = len(tasks)
        employee_id = employee.get('id')
        employee_name = employee.get('name')
        completed_tasks = []

        for task in tasks:
            if task.get('completed'):
                completed_tasks.append('\t ' + task.get('title'))
        total_completed = len(completed_tasks)
        print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                              total_completed,
                                                              task_total))
        print('\n'.join(completed_tasks))


if __name__ == '__main__':
    from requests import get
    from sys import argv

    if len(argv) == 2 and argv[1].isdigit():
        employee_info(argv[1])
