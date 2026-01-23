import allure
import pytest
from data import color_data
from methods.order_methods import OrderMethods


class TestOrderCreate:

    @allure.title('Проверка создания заказа')
    @allure.description('Нужно проверить: можно указать один из цветов — BLACK или GREY, оба цвета, не указывать цвет; тело ответа содержит track')
    @pytest.mark.parametrize("color", color_data)
    def test_creating_order_full_data_success(self, color):
        create_json, create_status = OrderMethods().create_order(color=color)
        assert create_json['track'] 
        assert create_status == 201