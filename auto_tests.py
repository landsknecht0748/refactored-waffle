import requests
import Configuration
import data

def create_new_order(body):
    return requests.post(Configuration.URL_SERVICE + Configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

def get_info_order(track):
    return requests.get(Configuration.URL_SERVICE + Configuration.GET_ORDER_PATH,
                        params={"t": track},
                        headers=data.headers)

def assert_code_success(response):
    assert response.status_code == 200
# Волков Никита, 9-я когорта — Финальный проект. Инженер по тестированию плюс
def test_order_create():
    order = create_new_order(data.order_body)
    order_track = order.json()['track']
    order_track_info = get_info_order(order_track)
    assert_code_success(order_track_info)
