import allure
from methods.order_methods import OrderMethods


class TestOrderList:
    
    @allure.title('Проверка списка заказов')
    @allure.description('Нужно проверить: в тело ответа возвращается список заказов; запрос возвращает правильный код ответа')
    def test_get_order_list_success(self):
        get_json, get_status = OrderMethods().get_order_list()
        assert get_json['orders'] and get_status == 200