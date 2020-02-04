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
        csv_f = []
        for task in wanted_tasks:
            csv_f.append({'id': employee_id,
                          'name': employee_username,
                          'completed': task.get('completed'),
                          'title': task.get('title')})

        key_item = ['id', 'name', 'completed', 'title']

        with open("{}.csv".format(employee_id), "w") as f:
            dictionary_csv = csv.DictWriter(f, key_item, quoting=csv.QUOTE_ALL)
            dictionary_csv.writerows(csv_f)

if __name__ == '__main__':
    from requests import get
    from sys import argv
    import csv

    if len(argv) == 2 and argv[1].isdigit():
        employee_info(argv[1])
