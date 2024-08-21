from Credits import rossko
import requests
import json

def parser (artic):
# URL для авторизации и получения токена
    auth_url = "https://www.masuma.ru/api/authorization"
    login = "evoverchenko@inbox.ru"
    password = "Qw123456"

    # Параметры для авторизации
    auth_params = {
        'login': login,
        'password': password
    }

    try:
        # Выполнение GET-запроса для авторизации
        response = requests.get(auth_url, params=auth_params)
        response.raise_for_status()  # Проверка на успешность ответа

        # Извлечение токена из ответа
        token = response.json().get('token')
        if not token:
            raise ValueError("Не удалось получить токен авторизации.")
    except requests.RequestException as e:
        print(f"Ошибка при запросе авторизации: {e}")
        return None
    except ValueError as e:
        print(e)
        return None

    # URL для получения данных по артикулу
    item_url = "https://www.masuma.ru/api/getitemsbyarticle"

    # Параметры для запроса данных по артикулу
    item_params = {
        'token': token,
        'article': article
    }

    try:
        # Выполнение POST-запроса для получения данных по артикулу
        response = requests.post(item_url, data=item_params)
        response.raise_for_status()

        # Извлечение списка запчастей из ответа
        items = response.json().get('items', [])
        if not items:
            print(f"Не найдены данные для артикула {article}")
            return None

        # Вывод информации о найденных запчастях
        for item in items:
            print(f"Артикул: {item.get('article')}, Цена: {item.get('price', 'Цена не указана')}")
        return items
    except requests.RequestException as e:
        print(f"Ошибка при запросе данных: {e}")
        return None

