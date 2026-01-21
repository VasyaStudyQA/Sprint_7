import allure
import pytest
from methods.courier_methods import CourierMethods
from data import courier_half_data
from data import ErrorMessages


class TestLoginCourier:

    @allure.title('Проверка авторизации курьера')
    @allure.description('Нужно проверить: курьер может авторизоваться; успешный запрос возвращает id.')
    def test_login_full_data_success(self):
        courier_data = CourierMethods().create_courier()[0]
        login_json, login_status = CourierMethods().login_courier(courier_data)
        assert login_json['id'] and login_status == 200

    @allure.title('Проверка авторизации курьера с незаполенным обязательным полем')
    @allure.description('Нужно проверить: для авторизации нужно передать все обязательные поля; если какого-то поля нет, запрос возвращает ошибку.')
    @pytest.mark.parametrize("courier_data", courier_half_data)
    def test_login_half_data_error(self, courier_data):
        login_json, login_status = CourierMethods().login_courier(courier_data)
        assert login_json['message'] == ErrorMessages.half_login_data and login_status == 400

    @allure.title('Проверка авторизации курьера с неправильным логином')
    @allure.description('Нужно проверить: система вернёт ошибку, если указать несуществующую или неправильную пару логин / пароль.')
    def test_login_wrong_login_error(self, courier):        
        login_data = {
            "login": courier["data"]["login"] + "123",
            "password": courier["data"]["password"]
        }
        login_json, login_status = CourierMethods().login_courier(login_data)        
        assert login_json["message"] == ErrorMessages.wrong_login_data and login_status == 404

    @allure.title('Проверка авторизации курьера с неправильным паролем')
    @allure.description('Нужно проверить: система вернёт ошибку, если указать несуществующую или неправильную пару логин / пароль.')
    def test_login_wrong_password_error(self, courier):
        login_data = {
            "login": courier["data"]["login"],
            "password": courier["data"]["password"] + "123"
        }
        login_json, login_status = CourierMethods().login_courier(login_data)        
        assert login_json["message"] == ErrorMessages.wrong_login_data and login_status == 404