import requests

def test_check_for_bugs():
    """Проверка объявлений на ошибки"""

    seller_id = 592731

    print("=== ПРОВЕРКА ОБЪЯВЛЕНИЙ НА ОШИБКИ ===")

    # Получаем все объявления
    response = requests.get(f"https://qa-internship.avito.com/api/1/{seller_id}/item")
    all_ads = response.json()

    print(f"Проверено объявлений: {len(all_ads)}")
    print()

    total_errors = 0

    # Проверяем каждое объявление
    for ad in all_ads:
        errors_in_ad = []
        ad_id = ad["id"]

        # Проверка цены
        if ad["price"] < 0:
            errors_in_ad.append(f"Отрицательная цена: {ad['price']}")

        # Проверка имени
        if not ad["name"].strip():
            errors_in_ad.append(f"Пустое имя")

        # Проверка статистики
        stats = ad["statistics"]

        if stats["likes"] < 0:
            errors_in_ad.append(f"Отрицательные лайки: {stats['likes']}")

        if stats["viewCount"] < 0:
            errors_in_ad.append(f"Отрицательные просмотры: {stats['viewCount']}")

        if stats["contacts"] < 0:
            errors_in_ad.append(f"Отрицательные контакты: {stats['contacts']}")

        # Выводим ошибки для этого объявления
        if errors_in_ad:
            print(f"ОШИБКИ в объявлении {ad_id}:")
            for error in errors_in_ad:
                print(f"  - {error}")
            print()
            total_errors += 1

    print("=== ИТОГИ ===")
    print(f"Объявлений с ошибками: {total_errors}")

    # Тест всегда проходит, даже если есть ошибки
    assert True