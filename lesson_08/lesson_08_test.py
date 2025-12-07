import requests

base_url = "https://ru.yougile.com"
token = "fI13J6p5MZIaumAUf0pRebqWb68eKhIgQaSlcf1b8nNqJDosudWUM3VkTGjm0Woa"


def test_1_post_positive():
    # Проверка создания проекта
    token = "fI13J6p5MZIaumAUf0pRebqWb68eKhIgQaSlcf1b8nNqJDosudWUM3VkTGjm0Woa"
    authorization = {}
    authorization["Authorization"] = f"Bearer {token}"
    project = {
        "title": "Проект"
        }

    get_projects = requests.get(base_url+"/api-v2/projects", headers=authorization)
    len_before = len(get_projects.json()["content"])
    make_project = requests.post(base_url+"/api-v2/projects", json=project, headers=authorization)
    len_after = len(requests.get(base_url+"/api-v2/projects", headers=authorization).json()["content"])
    status = make_project.status_code
    assert status == 201
    assert len_after - len_before == 1

def test_1_post_negative():
    # Создание проекта с пустым телом запроса
    token = "Wrong token"
    authorization = {}
    authorization["Authorization"] = f"Bearer {token}"
    project = {}
    
    make_project = requests.post(base_url+"/api-v2/projects", json=project, headers=authorization)
    status = make_project.status_code
    assert status == 401

def test_2_put_positive():
    # Изменение названия проекта
    authorization = {}
    authorization["Authorization"] = f"Bearer {token}"
    parameters ={
        id : "19cd68d2-dd55-4fac-8140-95e5d50c6e00"
    } 
    
    body = {
        "title": "Проектище"
    }
    
    make_project = requests.post(base_url+"/api-v2/projects", json=body, headers=authorization, params=parameters)
    status = make_project.status_code
    assert status == 201

def test_2_put_negative():
    # Изменение названия проекта с неправильным токеном
    token = "Wrong token"
    authorization = {}
    authorization["Authorization"] = f"Bearer {token}"
    parameters ={
        id : "19cd68d2-dd55-4fac-8140-95e5d50c6e00"
    } 
    body = {
        "title": "ГосУслуги 2.0"
    }
    
    make_project = requests.post(base_url+"/api-v2/projects", json=body, headers=authorization, params=parameters)
    status = make_project.status_code
    assert status == 401

def test_3_get_positive():
    # Запрос проекта по id
    authorization = {}
    authorization["Authorization"] = f"Bearer {token}"
    id = "19cd68d2-dd55-4fac-8140-95e5d50c6e00" 

    get_project = requests.get(base_url+"/api-v2/projects/"+id, headers=authorization)
    status = get_project.status_code
    assert status == 200

def test_3_get_negative():
    # Запрос проекта по неправильному id
    authorization = {}
    authorization["Authorization"] = f"Bearer {token}"
    id = "Wrong id" 

    get_project = requests.get(base_url+"/api-v2/projects/"+id, headers=authorization)
    status = get_project.status_code
    assert status == 404