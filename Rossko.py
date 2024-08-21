from Credits import rossko
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

def parser(artic):
    key1 = 'ad59f516976bf1c67e88cc350f47dd5d'
    key2 = 'be3c037947d8694a1f4667af2a0b783c'
    
    # URL WSDL
    url = 'http://api.rossko.ru/service/v2.1/GetSearch'
    
    # SOAP-XML сообщение
    soap_message = f"""<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v2="http://api.rossko.ru/service/v2.1/">
        <soap:Body>
            <v2:GetSearch>
                <v2:KEY1>{key1}</v2:KEY1>
                <v2:KEY2>{key2}</v2:KEY2>
                <v2:text>{artic}</v2:text>
                <v2:delivery_id>000000002</v2:delivery_id>
                <v2:address_id>112233</v2:address_id>
            </v2:GetSearch>
        </soap:Body>
    </soap:Envelope>"""
    
    # Заголовки для SOAP-запроса
    headers = {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': 'http://api.rossko.ru/service/v2.1/GetSearch'
    }
    
    try:
        # Отправка запроса
        response = requests.post(url, data=soap_message, headers=headers, timeout=1)
        
        # Проверка ответа
        if response.status_code == 200:
            print("Запрос выполнен успешно!")
            return response.text  # Возвращаем ответ в виде строки
        else:
            print(f"Ошибка выполнения запроса. Код ошибки: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при выполнении запроса: {e}")
        return None

