import configuration
import requests
import data


# Запрос на создание нового заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                         json=order_body)

# Запрос на получение трека заказа
def get_track_id(track_id):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDER,
                        params={"t": track_id})
