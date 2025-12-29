import requests
import random


def test_create_ad():
    """Создать объявление"""
    url = "https://qa-internship.avito.com/api/1/item"

    name = f"Item_{random.randint(1000, 9999)}"
    price = random.randint(10, 500)
    likes = random.randint(1, 50)
    views = random.randint(1, 200)
    contacts = random.randint(1, 10)

    print(f"\nСоздаем объявление: {name}, цена: {price}")
    print(f"Статистика: likes={likes}, views={views}, contacts={contacts}")

    data = {
        "sellerID": 592731,
        "name": name,
        "price": price,
        "statistics": {
            "likes": likes,
            "viewCount": views,
            "contacts": contacts
        }
    }

    r = requests.post(url, json=data)

    print(f"Статус код: {r.status_code}")
    print(f"Ответ: {r.json()}")

    assert r.status_code == 200
    assert "Сохранили объявление" in r.json()["status"]

    ad_id = r.json()["status"].split(" - ")[-1]
    print(f"Объявление создано. ID: {ad_id}")