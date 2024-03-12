# Наталья Кузнецова, 14-я когорта — Финальный проект. Инженер по тестированию плюс

import reques

def test_get_order_info_by_track():
    new_order = reques.creater_order()
    track = new_order.json()["track"]
    order_info = reques.get_order_info_by_track(track)
    assert order_info.status_code == 200