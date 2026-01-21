import allure
import pytest
from methods.courier_methods import CourierMethods
from data import courier_half_data


class TestLoginCourier:

    @allure.title('Проверка авторизации курьера')
    @allure.description('Нужно проверить: курьер может авторизоваться; успешный запрос возвращает id.')
    def test_login_full_data_success(self, courier):
        assert courier['courier_id'] and courier['login_status'] == 200

    @allure.title('Проверка авторизации курьера с незаполенным обязательным полем')
    @allure.description('Нужно проверить: для авторизации нужно передать все обязательные поля; если какого-то поля нет, запрос возвращает ошибку.')
    @pytest.mark.parametrize("courier_data", courier_half_data)
    def test_login_half_data_error(self, courier_data):
        login_json, login_status = CourierMethods().login_courier(courier_data)
        assert login_json['message'] == 'Недостаточно данных для входа' and login_status == 400

    @allure.title('Проверка авторизации курьера с неправильным логином или паролем')
    @allure.description('Нужно проверить: система вернёт ошибку, если указать несуществующую или неправильную пару логин / пароль.')
    @pytest.mark.parametrize("courier_data", ["wrong_login", "wrong_password"])
    def test_login_wrong_data_error(self, courier, courier_data):
        login = courier["data"]["login"]
        password = courier["data"]["password"]
        if courier_data == "wrong_login":
            login_data = {
                "login": login + "123",
                "password": password
            }
        else:
            login_data = {
                "login": login,
                "password": password + "123"
            }
        login_json, login_status = CourierMethods().login_courier(login_data)        
        assert login_json["message"] == "Учетная запись не найдена" and login_status == 404