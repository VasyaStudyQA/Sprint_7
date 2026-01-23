import pytest
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods


@pytest.fixture()
def courier():
    courier_data, create_json, create_status = CourierMethods().create_courier()
    login_json, login_status = CourierMethods().login_courier(courier_data)    
    yield {
        "data": courier_data,
        "create_response": create_json,
        "create_status": create_status,
        "login_response": login_json,
        "login_status": login_status,
        "courier_id": login_json['id']
    }
    CourierMethods().delete_courier(login_json['id'])

@pytest.fixture()
def courier_no_auth():
    courier_data, create_json, create_status = CourierMethods().create_courier()       
    yield {
        "data": courier_data,
        "create_response": create_json,
        "create_status": create_status,
    }
    login_json = CourierMethods().login_courier(courier_data)[0]
    CourierMethods().delete_courier(login_json['id'])

@pytest.fixture
def courier_cleanup():
    data = {}
    yield data
    login_json = CourierMethods().login_courier(data['courier_data'])[0]    
    CourierMethods().delete_courier(login_json['id'])

@pytest.fixture()
def order():
    create_json, create_status = OrderMethods().create_order(color=['BLACK'])
    get_order_json, get_order_status = OrderMethods().get_order_by_track(create_json['track'])
    yield {
        "create_response": create_json,
        "create_status": create_status,        
        "order_track": create_json['track'],
        "get_order_response": get_order_json,
        "get_order_status": get_order_status,        
        "order_id": get_order_json['order']['id']
    }