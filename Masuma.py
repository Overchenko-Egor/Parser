from Credits import masuma
import requests
import json

def get_token():
    #Адрес для получения токена
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
    response = requests.get(url_auth, params=params).json()

    # Выполнение POST запроса
    # response = requests.post(url, headers=headers, data=data)

    # Выполнение PUT запроса
    # response = requests.put(url, headers=headers, data=data)

    # Выполнение DELETE запроса
    # response = requests.delete(url, headers=headers)

    # Проверка кода ответа
    # print("Запрос выполнен успешно!")
    # print("Ответ сервера:", response['token'])  # Если ответ в формате JSON

    return (response['token'])


def parser(article):

    url_get = "https://masuma.ru/api/selectionbycar"
    token = get_token()
    print (token)
    print (article)

    params = {
        "token": token,
        # "article": article,
    }

    response = requests.get(url_get, params=params)
    print (response.status_code)

    # if response.status_code == 200:
    #     print("Запрос выполнен успешно!")
    #     print("Ответ сервера:", response['items'])
    # else:
    #     print(f"Ошибка выполнения запроса. Код ошибки: {response.status_code}")
    #     print("Текст ошибки:", response.text)

    

