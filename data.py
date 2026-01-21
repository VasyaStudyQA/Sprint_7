from methods.courier_methods import CourierMethods


courier_half_data = [{'login': CourierMethods().generate_courier_data()["login"], "password": ''}, 
                    {'login': '' ,'password': CourierMethods().generate_courier_data()["password"]}]

color_data = [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []]