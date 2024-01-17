# Анна Курочкина, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import pytest
import sender_stand_request


def test_track_get_order_information():
    # Выполнить запрос на создание заказа.
    response_create = sender_stand_request.post_new_order()
    # Сохранить номер трека заказа.
    track_number = response_create.json()["track"]
    # Создаем словарь для параметра запроса
    track = {"t": track_number}
    # Выполнить запрос на получение заказа по треку заказа.
    response_get = sender_stand_request.get_order(track)
    # Проверить, что код ответа равен 200.
    assert response_get.status_code == 200







