def read_file(file_path):
    # чтения файла построчно и преобразование в List словарей
    with open(file_path, mode="r") as file:
        data = file.readlines()
    return [eval(i.strip()[:-1]) for i in data]

def total_revenue(purchases):
    # общая выручка
    return sum([i["price"] * i["quantity"] for i in purchases])

def items_by_category(purchases):
    # ключ — категория, а значение — список уникальных товаров в этой категории.
    result = dict()
    for elem in purchases:
        result[elem['category']] = result.get(elem['category'], set())
        result[elem['category']].add(elem['item'])
    return result

def expensive_purchases(purchases, min_price):
    # покупки дороже min_price
        return [i for i in purchases if i["price"] >= min_price]

def average_price_by_category(purchases):
    # ключ — категория, а значение — список цен по категории.
    result = dict()
    sort_res = dict()
    for elem in purchases:
        result[elem['category']] = result.get(elem['category'], set())
        result[elem['category']].add(elem['price'])
    # в каждой категории считаем среднюю цену и добавляем значения в словарь
    for key, value in result.items():
        sort_res[key] = sum(value) / len(value)
    return sort_res

def ost_frequent_category(purchases):
    # Категория с наибольшим количеством проданных товаров
    result = {}
    for elem in purchases:
        result[elem['category']] = result.get(elem['category'], [])
        result[elem['category']].append(elem['quantity'])
    return max(result)

# путь к файлу
file_path = "purchases.txt"
# мин.цена
price_min = 1

purchases = read_file(file_path)
print(purchases)
print(f"Общая выручка: {total_revenue(purchases)}")
print(f"Товары по категориям: {items_by_category(purchases)}")
print(f"Покупки дороже {price_min}: {expensive_purchases(purchases, price_min)}")
print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
print(f"Категория с наибольшим количеством проданных товаров: {ost_frequent_category(purchases)}")




