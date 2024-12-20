import requests
from bs4 import BeautifulSoup

def parser ():
    # Константы
    url_login = "https://masuma.ru/login_check"
    url_main = "https://masuma.ru"
    headers = {
        "Host": "masuma.ru",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://masuma.ru",
        "Referer": "https://masuma.ru/login",
        "Accept-Language": "ru-RU,ru;q=0.9",
        "Accept-Encoding": "gzip, deflate, br"
    }

    data = {
        "_csrf_token": "a1DUUklaPPRc7HgX1u1ZPi-u7IAe7drTPkPfWDY5H2U",
        "_username": "evoverchenko@inbox.ru",
        "_password": "Qw123456",
        "_remember_me": "1"
    }

    # Сессия
    with requests.Session() as session:
        # Авторизация
        response = session.post(url_login, headers=headers, data=data)
        if response.status_code == 200:
            print("Авторизация прошла успешно")
        else:
            print(f"Ошибка авторизации: {response.status_code}")
            exit()

        # Парсинг главной страницы
        response = session.get(url_main, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            print("HTML главной страницы:")
            print(soup.prettify())
        else:
            print(f"Ошибка доступа к главной странице: {response.status_code}")










# from Credits import masuma
# import requests
# import json
# from bs4 import BeautifulSoup


# def get_token():
#     #Адрес для получения токена
#     url_auth = "https://masuma.ru/api/authorization"

#     # Заголовки запроса
#     headers = {
#         "User-Agent": "your-user-agent",
#         "Authorization": "Bearer your-token",
#     }

#     # Параметры запроса (для GET запроса)
#     params = {
#         "login": masuma.login,
#         "password": masuma.password,
#     }

#     # Тело запроса (для POST, PUT, PATCH запросов)
#     data = {
#         "key1": "value1",
#         "key2": "value2",
#     }

#     # Выполнение GET запроса
#     response = requests.get(url_auth, params=params).json()

#     # Выполнение POST запроса
#     # response = requests.post(url, headers=headers, data=data)

#     # Выполнение PUT запроса
#     # response = requests.put(url, headers=headers, data=data)

#     # Выполнение DELETE запроса
#     # response = requests.delete(url, headers=headers)

#     # Проверка кода ответа
#     # print("Запрос выполнен успешно!")
#     # print("Ответ сервера:", response['token'])  # Если ответ в формате JSON

#     return (response['token'])


# def parser(article):

#     url_get = "https://masuma.ru/api/selectionbycar"
#     token = get_token()
#     print (token)
#     print (article)

#     params = {
#         "token": token,
#         # "article": article,
#     }

#     response = requests.get(url_get, params=params)
#     print (response.status_code)

#     # if response.status_code == 200:
#     #     print("Запрос выполнен успешно!")
#     #     print("Ответ сервера:", response['items'])
#     # else:
#     #     print(f"Ошибка выполнения запроса. Код ошибки: {response.status_code}")
#     #     print("Текст ошибки:", response.text)

    







# def parser(article):
#     login_url = "https://masuma.ru/login"
#     data_url = "https://masuma.ru/personal/orders"

#     # Создание сессии
#     session = requests.Session()

#     # Получение страницы логина
#     login_page = session.get(login_url)
#     login_soup = BeautifulSoup(login_page.content, 'html.parser')

#     login_form = login_soup.find('form', {'class': 'authorization-form'})
#     if login_form is None:
#         print("Форма логина не найдена. Проверьте HTML страницу.")
#         exit()

#     csrf_token_input = login_form.find('input', {'name': '_csrf_token'})
#     if csrf_token_input is None:
#         print("Не удалось найти CSRF токен. Проверьте HTML страницу.")
#         exit()

#     email_input = login_form.find('input', {'name': '_username'})
#     print (email_input)
#     password_input = login_form.find('input', {'type': 'password'})
#     print (password_input)
#     submit_button = login_form.find('button', {'type': 'submit'})
#     print (submit_button)

#     # Проверка наличия необходимых элементов
#     if email_input is None or password_input is None or submit_button is None:
#         print("Не удалось найти необходимые поля формы. Проверьте HTML страницу.")
#         exit()

#     login_data = {
#     '_csrf_token': csrf_token_input['value'],
#     '_username': masuma.login,
#     '_password': masuma.password,
#     '_remember_me': '1'  # Если нужно, чтобы пользователь остался авторизованным
#     }

#     # Заголовки (если требуется)
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'Referer': login_url
#     }

#     response = session.post(login_url, data=login_data, headers=headers)
    
    
