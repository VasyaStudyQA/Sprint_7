import allure
from methods.order_methods import OrderMethods


class TestOrderByTrack:

    @allure.title('Получить заказ по его номеру')
    @allure.description('Нужно проверить: успешный запрос возвращает объект с заказом; запрос возвращает правильный код ответа')
    def test_get_order_by_track_full_data_success(self, order):
        assert order['get_order_response']['order'] and order['get_order_status'] == 200

    @allure.title('Получить заказ без номера заказа')
    @allure.description('Нужно проверить: запрос без номера заказа возвращает ошибку; запрос возвращает правильный код ответа')
    def test_get_order_by_track_no_data_error(self):
        get_order_json, get_order_status = OrderMethods().get_order_by_track('')
        assert get_order_json['message'] == 'Недостаточно данных для поиска' and get_order_status == 400

    @allure.title('Получить заказ с несуществующим номером')
    @allure.description('Нужно проверить: запрос с несуществующим заказом возвращает ошибку; запрос возвращает правильный код ответа')
    def test_get_order_by_track_wrong_data_error(self):
        get_order_json, get_order_status = OrderMethods().get_order_by_track(0)
        assert get_order_json['message'] == 'Заказ не найден' and get_order_status == 404