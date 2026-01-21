import allure
import pytest
from methods.courier_methods import CourierMethods
from data import ErrorMessages, courier_half_data


class TestCreateCourier:

    @allure.title('Проверка создания курьера')
    @allure.description('Нужно проверить: курьера можно создать; запрос возвращает правильный код ответа; успешный запрос возвращает {"ok":true}')
    def test_creating_courier_full_data_success(self):
        create_json, create_status = CourierMethods().create_courier()[1:]
        assert create_json == {'ok': True} and create_status == 201

    @allure.title('Проверка создания курьера с занятым логином')
    @allure.description('Нужно проверить: нельзя создать двух одинаковых курьеров; если создать пользователя с логином, который уже есть, возвращается ошибка.')
    def test_creating_courier_used_data_error(self):
        used_data = CourierMethods().create_courier()[0]
        create_json, create_status = CourierMethods().create_courier(used_data)[1:]
        assert create_json['message'] == ErrorMessages.used_create_courier_data and create_status == 409

    @allure.title('Проверка создания курьера с незаполенным обязательным полем')
    @allure.description('Нужно проверить: чтобы создать курьера, нужно передать в ручку все обязательные поля; если одного из полей нет, запрос возвращает ошибку.')
    @pytest.mark.parametrize("courier_data", courier_half_data)
    def test_creating_courier_half_data_error(self, courier_data):
        create_json, create_status = CourierMethods().create_courier(courier_data)[1:]
        assert create_json['message'] == ErrorMessages.half_create_courier_data and create_status == 400