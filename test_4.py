import requests
import random


def test_get_stats():
    """Получить статистику случайного объявления"""
    seller_id = 592731

    print(f"\n1. Ищем объявления продавца {seller_id}")
    r = requests.get(f"https://qa-internship.avito.com/api/1/{seller_id}/item")

    ads = r.json()
    print(f"   Найдено объявлений: {len(ads)}")

    if len(ads) == 0:
        print("   Нет объявлений, создаем новое...")
        data = {
            "sellerID": seller_id,
            "name": f"Test_Item_{random.randint(100, 999)}",
            "price": random.randint(100, 500),
            "statistics": {
                "likes": random.randint(1, 10),
                "viewCount": random.randint(1, 50),
                "contacts": random.randint(1, 5)
            }
        }
        r_create = requests.post("https://qa-internship.avito.com/api/1/item", json=data)
        ad_id = r_create.json()["status"].split(" - ")[-1]
        print(f"   Создано объявление с ID: {ad_id}")
        selected_ad = {"id": ad_id, "name": data["name"]}
    else:
        # Берем случайное объявление
        selected_ad = random.choice(ads)
        ad_id = selected_ad["id"]
        print(f"   Выбрано случайное объявление:")
        print(f"   ID: {ad_id}")

    # Получаем статистику
    print(f"\n2. Получаем статистику для ID: {ad_id}")
    r_stats = requests.get(f"https://qa-internship.avito.com/api/1/statistic/{ad_id}")

    print(f"   Статус код: {r_stats.status_code}")

    stats_data = r_stats.json()
    stats = stats_data[0]

    print(f"\n3. Статистика товара '{selected_ad['name']}':")
    print(f"   - likes: {stats['likes']}")
    print(f"   - viewCount: {stats['viewCount']}")
    print(f"   - contacts: {stats['contacts']}")

    assert r_stats.status_code == 200
    print(f"\nOK - Статистика получена")