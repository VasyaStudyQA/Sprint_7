import random
import string
import allure
import requests
from urls import BASE_URL, COURIER_URL

class CourierMethods:
    def __init__(self):
        self.url = BASE_URL+COURIER_URL

    @allure.step('Создать курьера')
    def create_courier(self, params=None):
        if params is None:
            params = self.generate_courier_data()
        response = requests.post(
            self.url, data=params
        )
        try:
            return params, response.json(), response.status_code
        except:
            return response.text, response.status_code
        

    @allure.step('Авторизация курьера')  
    def login_courier(self, params):
        login_data = {
            'login': params['login'],
            'password': params['password']
        }
        response = requests.post(
            self.url+'login', data=login_data
        )
        try:
            return response.json(), response.status_code
        except:
            return response.text, response.status_code
        

    @allure.step('Удалить курьера')  
    def delete_courier(self, courier_id):
        delete_params = {
            'id': courier_id
        }
        response = requests.delete(
            self.url+str(courier_id), data=delete_params
        )
        try:
            return response.json(), response.status_code
        except:
            return response.text, response.status_code

    
    @staticmethod
    def generate_courier_data():
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }        

        # возвращаем список
        return payload   