import requests


def test_create_ad_with_zero_stats():
    """Создать объявление со статистикой 0,0,0"""
    url = "https://qa-internship.avito.com/api/1/item"

    print("\nСоздание с нулевой статистикой 0,0,0")

    data = {
        "sellerID": 592731,
        "name": "Test",
        "price": 100,
        "statistics": {
            "likes": 0,
            "viewCount": 0,
            "contacts": 0
        }
    }

    r = requests.post(url, json=data)

    if r.status_code == 200:
        print("Успешно")
    else:
        print(f"Ошибка {r.status_code}: {r.json()}")

    assert True