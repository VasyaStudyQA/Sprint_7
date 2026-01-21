import allure
from methods.order_methods import OrderMethods
from data import ErrorMessages


class TestOrderAccept:

    @allure.title('Проверка принятия заказа')
    @allure.description('Нужно проверить: успешный запрос возвращает{"ok":true}; запрос возвращает правильный код ответа')
    def test_accept_order_full_data_success(self, courier, order):
        accept_json, accept_status = OrderMethods().accept_order(order['order_id'], courier['courier_id'])
        assert accept_json == {"ok":True} and accept_status == 200

    @allure.title('Проверка принятия заказа без id курьера')
    @allure.description('Нужно проверить: если не передать id курьера, запрос вернёт ошибку; запрос возвращает правильный код ответа')
    def test_accept_order_no_courier_id_error(self, order):
        accept_json, accept_status = OrderMethods().accept_order(order['order_id'], '')
        assert accept_json['message'] == ErrorMessages.accept_order_no_courier and accept_status == 400

    @allure.title('Проверка принятия заказа с неверным id курьера')
    @allure.description('Нужно проверить: если передать неверный id курьера, запрос вернёт ошибку; запрос возвращает правильный код ответа')
    def test_accept_order_wrong_courier_id_error(self, order):
        accept_json, accept_status = OrderMethods().accept_order(order['order_id'], 0)
        assert accept_json['message'] == ErrorMessages.accept_order_wrong_courier_id and accept_status == 404

    @allure.title('Проверка принятия заказа без id заказа')
    @allure.description('Нужно проверить: если не передать id заказа, запрос вернёт ошибку; запрос возвращает правильный код ответа')
    def test_accept_order_no_order_id_error(self, courier):
        accept_json, accept_status = OrderMethods().accept_order('', courier['courier_id'])
        assert accept_json['message'] == ErrorMessages.not_found and accept_status == 404

    @allure.title('Проверка принятия заказа с неверным id заказа')
    @allure.description('Нужно проверить: если передать неверный id заказа, запрос вернёт ошибку; запрос возвращает правильный код ответа')
    def test_accept_order_wrong_order_id_error(self, courier):
        accept_json, accept_status = OrderMethods().accept_order(0, courier['courier_id'])
        assert accept_json['message'] == ErrorMessages.accept_order_wrong_order_id and accept_status == 404        