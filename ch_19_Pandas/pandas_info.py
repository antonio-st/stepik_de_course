
# --------------- series ---------------
# без индекса
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series)

# с индексом
index = ["a", "b", "c", "d", "e"]
series_w_index = pd.Series(data, index=index)
print(series_w_index)

# series из словаря
data_2 = {'e': 10, 'd': 20, 'c': 30, 'b': 40, 'a': 50}
series_from_dict = pd.Series(data_2)
print(series_from_dict)

# вывод без dtype: int64
print(series_from_dict.to_string())

print(f"Обращение по индексу\n {series_from_dict['a']}")
print(f"Обращение по индексу к 3 элементам\n {series_from_dict[['a', 'b', 'c']]}")
print(f"Обращение по номеру\n {series_from_dict[2]}")

another_series = pd.Series([5, 15, 25, 35, 45], index=['a', 'b', 'c', 'd', 'e'])

print("Сложение Series\n", series_w_index + another_series)

print(f"Умножение Series\n{series_from_dict * 2}")

print("Создание Series с отсутствующими значениями")

data_nan = [10, 20, None, 40, 50]
index_n = ['a', 'b', 'c', 'd', 'e']

series_with_nan = pd.Series(data_nan, index=index_n)
print("Series с отсутствующими значениями:")
print(series_with_nan)

fil_series = series_with_nan.fillna(0)
print(fil_series)

print(f"Удаление NaN:\n{series_with_nan.dropna()}")