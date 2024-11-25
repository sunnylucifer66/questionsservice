import requests
import json

def send_request(register=False, login=False, generate_advice=False):
    headers = {"Content-Type": "application/json"}
    token = None  # Изначально токен пустой

    if register:
        url = "http://127.0.0.1:8000/register"
        data = {
            "email": "dmitriy@gmail.com",
            "password": "dmitriy123",
            "name": "Dmitry Grishin",
            "age": 4,
            "interests": "Программирование",
            "goals": "Изучение SQL Alchemy"
        }
        print(f"Отправляем запрос на {url} с данными: {data}")
        try:
            response = requests.post(url, headers=headers, json=data)
            print(f"Код статуса: {response.status_code}")
            print("JSON-ответ:", response.json())
        except Exception as e:
            print(f"Ошибка соединения: {e}")
            return

    if login:
        url = "http://127.0.0.1:8000/login"
        data = {
            "email": "dmitriy@gmail.com",
            "password": "dmitriy123"
        }
        print(f"Отправляем запрос на {url} с данными: {data}")
        try:
            response = requests.post(url, headers=headers, json=data)
            print(f"Код статуса: {response.status_code}")
            print("JSON-ответ:", response.json())
            # Получаем токен из ответа и сохраняем
            if response.status_code == 200:
                token = response.json().get("access_token")
                print(f"Получен токен: {token}")
        except Exception as e:
            print(f"Ошибка соединения: {e}")
            return

    if generate_advice:
        if not token:
            print("Ошибка: Необходим токен для выполнения запроса")
            return

        url = "http://127.0.0.1:8000/generate_advice"
        data = {
            "user_id": 2,
            "query": "Ты можешь рассказать про игру STALKER 2?"
        }
        headers["Authorization"] = f"Bearer {token}"  # Добавляем токен в заголовок
        print(f"Отправляем запрос на {url} с данными: {data}")
        try:
            response = requests.post(url, headers=headers, json=data)
            print(f"Код статуса: {response.status_code}")
            print("JSON-ответ:", response.json())
        except Exception as e:
            print(f"Ошибка соединения: {e}")
            return

# Пример вызова функции для генерации совета
send_request(login=True)
