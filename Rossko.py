from Credits import rossko
import requests
import json
import xmltodict

def parser(artic):
    key1 = 'ad59f516976bf1c67e88cc350f47dd5d'
    key2 = 'be3c037947d8694a1f4667af2a0b783c'
    
    # URL WSDL
    url = 'http://api.rossko.ru/service/v2.1/GetSearch'

    # SOAP-XML сообщение
    soap_message = f"""<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tns="http://api.rossko.ru/">
        <soap:Body>
            <tns:GetSearch>
                <tns:KEY1>{key1}</tns:KEY1>
                <tns:KEY2>{key2}</tns:KEY2>
                <tns:text>{artic}</tns:text>
                <tns:delivery_id>000000001</tns:delivery_id>
            </tns:GetSearch>
        </soap:Body>
    </soap:Envelope>"""

    headers = {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': 'http://api.rossko.ru/service/v2.1/GetSearch'
    }

    try:
        # Отправка POST-запроса с XML в теле
        response = requests.post(url, data=soap_message, headers=headers)
        
        # Вывод статуса и текста ответа для отладки
        print("Статус ответа:", response.status_code)
        # print("Текст ответа:", response.text)
        
        if response.status_code == 200:
            # Парсинг XML в словарь
            response_dict = xmltodict.parse(response.text)
            
            # Преобразование словаря в JSON
            response_json = json.dumps(response_dict, indent=4, ensure_ascii=False)
            
            # Сохранение JSON в файл
            with open('response.json', 'w', encoding='utf-8') as f:
                f.write(response_json)
            
            data = json.loads(response_json)

            # Извлекаем первое поле name и price
            first_part = data['SOAP-ENV:Envelope']['SOAP-ENV:Body']['ns1:GetSearchResponse']['ns1:SearchResult']['ns1:PartsList']['ns1:Part'][0]
            first_name = first_part['ns1:crosses']['ns1:Part']['ns1:name']
            first_price = first_part['ns1:crosses']['ns1:Part']['ns1:stocks']['ns1:stock'][0]['ns1:price']

            # Выводим на консоль
            print(f"Первое поле name: {first_name}")
            print(f"Первое поле price: {first_price}")


            return response_json
        else:
            print(f"Ошибка выполнения запроса. Код ошибки: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при выполнении запроса: {e}")
        return None

