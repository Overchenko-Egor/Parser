from Credits import masuma
import requests

def parser():
    # URL к которому делаем запрос
    url_api = "https://masuma.ru/api"
    url_auth = "https://masuma.ru/api/authorization"

    # Заголовки запроса
    headers = {
        "User-Agent": "your-user-agent",
        "Authorization": "Bearer your-token",
    }

    # Параметры запроса (для GET запроса)
    params = {
        "login": masuma.login,
        "password": masuma.password,
    }

    # Тело запроса (для POST, PUT, PATCH запросов)
    data = {
        "key1": "value1",
        "key2": "value2",
    }

    # Выполнение GET запроса
    response = requests.get(url_auth, params=params)

    # Выполнение POST запроса
    # response = requests.post(url, headers=headers, data=data)

    # Выполнение PUT запроса
    # response = requests.put(url, headers=headers, data=data)

    # Выполнение DELETE запроса
    # response = requests.delete(url, headers=headers)

    # Проверка кода ответа
    if response.status_code == 200:
        print("Запрос выполнен успешно!")
        print("Ответ сервера:", response.json())  # Если ответ в формате JSON
    else:
        print(f"Ошибка выполнения запроса. Код ошибки: {response.status_code}")
        print("Текст ошибки:", response.text)
