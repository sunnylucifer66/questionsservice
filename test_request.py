import requests
import json

def send_request(register=False, login=False, generate_advice=False):

    headers = {"Content-Type": "application/json"}

    if register:
        url = "http://127.0.0.1:8000/register"
        data = {"email": "dmitryxyilo@gmail.com",
                "password": "dmitryxyilo123",
                "name": "Dmitry Xyilo",
                "age": 4,
                "interests": "программирование",
                "goals": "изучение SQL Alchemy"}
    if login:
        url = "http://127.0.0.1:8000/login"
        data = {"email": "dmitryxyilo@gmail.com",
                "password": "dmitryxyilo123"}
    if generate_advice:
        url = "http://127.0.0.1:8000/generate_advice"
        data = {"user_id": 1,
                "query": "Чат привет, расскажи мне анекдот)"}

    payload = data
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    print(f"Status Code: {response.status_code}")

    # Если статус 200, пробуем вывести ответ как JSON
    if response.status_code == 200:
        try:
            print(response.json())
        except requests.exceptions.JSONDecodeError:
            print("Response is not JSON, raw response text:")
            print(response.text)
    else:
        print(f"Request failed with status code: {response.status_code}")
        print("Response text:", response.text)

send_request(generate_advice=True)
