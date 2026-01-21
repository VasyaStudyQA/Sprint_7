import random
import string
import allure
import requests
from urls import BASE_URL, ORDERS_URL


class OrderMethods:
    def __init__(self):
        self.url = BASE_URL+ORDERS_URL

    @allure.step('Создать заказ')
    def create_order(self, color=None, params=None):
        if params is None:
            params = self.generate_order_data(color)
        response = requests.post(
            self.url, json=params
        )
        try:
            return response.json(), response.status_code
        except:
            return response.text, response.status_code     
        
    @allure.step('Получить список заказов')
    def get_order_list(self, params=None):
        response = requests.get(
            self.url, data=params
        )
        try:
            return response.json(), response.status_code
        except:
            return response.text, response.status_code
        
    @allure.step('Принять заказ')
    def accept_order(self, order_id, courier_id):
        response = requests.put(
            f'{self.url}accept/{order_id}?courierId={courier_id}'
        )
        try:
            return response.json(), response.status_code
        except:
            return response.text, response.status_code
        
    @allure.step('Получить заказ по трек-номеру')
    def get_order_by_track(self, track):
        response = requests.get(
            f'{self.url}track?t={track}'
        )
        try:
            return response.json(), response.status_code
        except:
            return response.text, response.status_code

    
    @staticmethod
    def generate_order_data(color):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # генерируем необходимы поля
        firstName = generate_random_string(10)
        lastName = generate_random_string(10)
        address = generate_random_string(10)
        metroStation = random.randint(1, 50)
        phone = random.randint(80000000000, 89999999999)
        rentTime = random.randint(1, 10)
        deliveryDate = f'2026-{random.randint(1, 12)}-{random.randint(1, 28)}'
        comment = generate_random_string(10)
        color = color

        # собираем тело запроса
        order_data = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": color
            }     

        # возвращаем список
        return order_data  