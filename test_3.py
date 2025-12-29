import requests
import random


def test_get_ads_by_seller():
    """Все объявления продавца"""
    seller_id = random.randint(111111, 999999)

    print(f"1. Создаем объявления для seller_id={seller_id}")

    # Создаем 2 объявления
    for i in range(2):
        data = {
            "sellerID": seller_id,
            "name": f"Item_{i + 1}",
            "price": random.randint(100, 500),
            "statistics": {
                "likes": random.randint(1, 10),
                "viewCount": random.randint(1, 50),
                "contacts": random.randint(1, 5)
            }
        }
        r = requests.post("https://qa-internship.avito.com/api/1/item", json=data)
        print(f"   Создано: {data['name']}, Цена: {data['price']}")

    # Получаем объявления
    print(f"\n2. Получаем ВСЕ объявления продавца {seller_id}")
    r = requests.get(f"https://qa-internship.avito.com/api/1/{seller_id}/item")

    print(f"   Статус код: {r.status_code}")

    ads = r.json()
    print(f"   Всего объявлений: {len(ads)}")

    print(f"\n3. Список объявлений:")
    for i, ad in enumerate(ads, 1):
        print(f"   {i}. ID: {ad['id']}")
        print(f"      Название: {ad['name']}")
        print(f"      Цена: {ad['price']}")
        print(f"      Создано: {ad['createdAt'][:19]}")
        print(
            f"      Статистика: likes={ad['statistics']['likes']}, views={ad['statistics']['viewCount']}, contacts={ad['statistics']['contacts']}")

    assert r.status_code == 200
    print(f"\nOK - Получены все объявления")