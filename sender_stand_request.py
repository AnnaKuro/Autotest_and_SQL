# Анна Курочкина, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data

# Запрос на создание заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  # подставляем полный url
                         json=data.order_body,      # тут тело
                         headers=data.headers)       # а здесь заголовки


def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK,     # подставляем полный url
                         params=track,     # подставляем трек номер
                         headers=data.headers)            # а здесь заголовки

