import allure
from data import ErrorMessages
from methods.courier_methods import CourierMethods


class TestDeleteCourier:

    @allure.title('Проверка удаления курьера')
    @allure.description('Нужно проверить: успешный запрос возвращает {"ok":true}; запрос возвращает правильный код ответа')
    def test_deleting_courier_full_data_success(self, courier):
        delete_json, delete_status = CourierMethods().delete_courier(courier['courier_id'])
        assert delete_json == {'ok': True} and delete_status == 200

    @allure.title('Проверка удаления курьера с несуществующим id')
    @allure.description('Нужно проверить: если отправить запрос с несуществующим id, вернётся ошибка; запрос возвращает правильный код ответа')
    def test_deleting_courier_full_data_error(self):
        delete_json, delete_status = CourierMethods().delete_courier(0)
        assert delete_json['message'] == ErrorMessages.no_courier_id and delete_status == 404

    @allure.title('Проверка удаления курьера без id')
    @allure.description('Нужно проверить: если отправить запрос без id, вернётся ошибка; запрос возвращает правильный код ответа')
    def test_deleting_courier_no_data_error(self):
        delete_json, delete_status = CourierMethods().delete_courier('')
        assert delete_json['message'] == ErrorMessages.not_found and delete_status == 404