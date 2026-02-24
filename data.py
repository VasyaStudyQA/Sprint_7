from methods.courier_methods import CourierMethods


courier_half_data = [{'login': CourierMethods().generate_courier_data()["login"], "password": ''}, 
                    {'login': '' ,'password': CourierMethods().generate_courier_data()["password"]}]

color_data = [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []]

class ErrorMessages:
    not_found = 'Not Found.'

    used_create_courier_data = 'Этот логин уже используется. Попробуйте другой.'
    half_create_courier_data = 'Недостаточно данных для создания учетной записи'
    no_courier_id = 'Курьера с таким id нет.'
    half_login_data ='Недостаточно данных для входа'
    wrong_login_data = "Учетная запись не найдена"
    
    accept_order_no_courier = 'Недостаточно данных для поиска'
    accept_order_wrong_courier_id = 'Курьера с таким id не существует'
    accept_order_wrong_order_id = 'Заказа с таким id не существует'