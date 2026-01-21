import allure
import pytest
from methods.courier_methods import CourierMethods
from data import courier_half_data


class TestCreateCourier:

    @allure.title('Проверка создания курьера')
    @allure.description('Нужно проверить: курьера можно создать; запрос возвращает правильный код ответа; успешный запрос возвращает {"ok":true}')
    def test_creating_courier_full_data_success(self, courier):
        assert len(courier['data']['login'])==10 and courier['create_response'] == {'ok': True} and courier['create_status'] == 201

    @allure.title('Проверка создания курьера с занятым логином')
    @allure.description('Нужно проверить: нельзя создать двух одинаковых курьеров; если создать пользователя с логином, который уже есть, возвращается ошибка.')
    def test_creating_courier_used_data_error(self, courier):
        used_data = courier["data"].copy()
        create_json, create_status = CourierMethods().create_courier(used_data)[1:]
        assert create_json['message'] == "Этот логин уже используется. Попробуйте другой." and create_status == 409

    @allure.title('Проверка создания курьера с незаполенным обязательным полем')
    @allure.description('Нужно проверить: чтобы создать курьера, нужно передать в ручку все обязательные поля; если одного из полей нет, запрос возвращает ошибку.')
    @pytest.mark.parametrize("courier_data", courier_half_data)
    def test_creating_courier_half_data_error(self, courier_data):
        create_json, create_status = CourierMethods().create_courier(courier_data)[1:]
        assert create_json['message'] == "Недостаточно данных для создания учетной записи" and create_status == 400