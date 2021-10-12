#2.6.1. Сохраните JSON-набор, полученный через внешний API, в файл
import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
with open("response_result.json", "w") as json_file:
    json.dump(response.json(), json_file)

#2.6.2. Посчитайте количество уникальных пользователей в этом наборе
import json

def count_unique_users(json_lst):
    users = {}
    for elem in json_lst:
        if elem["userId"] in users:
            users[elem["userId"]] += 1
        else:
            users[elem["userId"]] = 1
    
    return len(users)
    
with open("response_result.json", "r") as json_file:
    response_result = json.load(json_file)
    
print(f'Количество уникальных пользователей: {count_unique_users(response_result)}')

#2.6.3. Посчитайте для каждого пользователя, сколько у него оригинальных задач, и сколько из них выполнено
import json

def count_unique_completed_tasks(json_lst):
    users = {}
    for elem in json_lst:
        users[elem["userId"]] = {"task_count": 0, "completed": 0}
    for elem in json_lst:
        users[elem["userId"]]["task_count"] += 1
        if elem['completed']:
            users[elem["userId"]]["completed"] += 1
    return users
       
with open("response_result.json", "r") as json_file:
    response_result = json.load(json_file)

users_dict = count_unique_completed_tasks(response_result)    

for key, value in users_dict.items():
    task_count, completed = value.values()
    print(f'Пользователь: {key} оригинальных задач: {task_count} из них выполнено: {completed}')