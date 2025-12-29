import requests
import random


def test_get_ad_by_id():
    """Получить объявление по ID"""
    url = "https://qa-internship.avito.com/api/1/item"

    # Создаем
    name = f"Test_{random.randint(1000, 9999)}"
    price = random.randint(50, 300)

    print(f"\n1. Создаем объявление: {name}, цена: {price}")

    data = {
        "sellerID": 592731,
        "name": name,
        "price": price,
        "statistics": {
            "likes": random.randint(1, 30),
            "viewCount": random.randint(1, 150),
            "contacts": random.randint(1, 8)
        }
    }

    r_create = requests.post(url, json=data)
    ad_id = r_create.json()["status"].split(" - ")[-1]
    print(f"ID созданного объявления: {ad_id}")

    # Получаем
    print(f"\n2. Получаем объявление по ID {ad_id}")
    r_get = requests.get(f"{url}/{ad_id}")

    print(f"Статус код: {r_get.status_code}")

    response_data = r_get.json()
    print(f"Данные объявления: {response_data}")

    assert r_get.status_code == 200
    assert response_data[0]["id"] == ad_id
    assert response_data[0]["name"] == name
    assert response_data[0]["price"] == price

    print(f"Объявление получено. Название: {response_data[0]['name']}, Цена: {response_data[0]['price']}")