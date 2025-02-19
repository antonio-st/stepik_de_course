import pandas as pd
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

# ----------------- DF -----------------------------------

data = {
    "Name" : ["Alice", "Bob", "Cathy", "Robert"],
    "Age" : [25, 35, 28, 39],
    "City" : ["New-York", "Boston", "California", "Chicago"]
}

df = pd.DataFrame(data)

print(f"DF из dict:\n{df}")

data_2 = [
    ["Alice", 28, "New-York"],
    ["Michael", 36, "Boston"],
    ["Kate", 26, "California"],
    ["Robert", 38, "Chicago"],
]

df_from_list = pd.DataFrame(data_2, columns=["Name", "Age", "City"])
print(f"DF из list:\n{df_from_list}")


# чтение из файла
df = pd.read_csv("data.csv", sep=",")

print(df)
print(df.head(2))
print(df.tail(2))

# вывод одного / нескольких столбцов
print("---------- вывод одного / нескольких столбцов ---------- ")
print(df["player_id"])
print(df[["player_id", "reb_per_game"]])

print("---------- инфо df ---------------")
print(df.describe())
print("-------------------------")
print(df.info())

# добавляем столбцы
print("---------- добавляем столбцы/ удаляем ----------")
df["salary"] = [50000, 60000, 57000, 65000]
print(df)

df = df.drop("salary", axis=1)
print(df)

print("Строка по индексу")
df = df.drop(2, axis=0)
print(df)


# --------------------- concat -----------------------------

df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
}, index=[0, 1, 2, 3])

df2 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7']
}, index=[4, 5, 6, 7])

print(df1)
print(df2)

# Конкатенация двух DataFrame по строкам (axis=0)
result_concat = pd.concat([df1, df2], axis=0)
print("Конкатенация по строкам:\n", result_concat)

# Конкатенация двух DataFrame по столбцам (axis=1)
result_concat_cols = pd.concat([df1, df2], axis=1)
print("\nКонкатенация по столбцам:\n", result_concat_cols)


# --------------------- merge ------------------------------


df1 = pd.DataFrame({
    'Key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

df2 = pd.DataFrame({
    'Key': ['K0', 'K1', 'K2', 'K4'],
    'C': ['C0', 'C1', 'C2', 'C4'],
    'D': ['D0', 'D1', 'D2', 'D4']
})

print(df1,"\n")
print(df2)

# Слияние двух DataFrame по общему столбцу 'Key'
result_merge = pd.merge(df1, df2, on='Key', how='inner')
print("\nСлияние по общему столбцу 'Key' (inner join):\n", result_merge)

# Слияние двух DataFrame с внешним объединением (outer join)
result_merge_outer = pd.merge(df1, df2, on='Key', how='outer')
print("\nСлияние с внешним объединением (outer join):\n", result_merge_outer)



# --------------------- манипуляции с данными ------------------------

import numpy as np

# Создание DataFrame с пропущенными значениями
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, 2, 3, 4, 5]
})

print(df)

# Удаление строк с любыми пропущенными значениями
df_drop_na = df.dropna()
print(f"df очищенный от пропусков\n{df_drop_na}")

# Удаление столбцов, содержащих пропущенные значения

df_drop_na_col = df.dropna(axis=1)
print(f"Удаление столбцов, содержащих пропущенные значения:\n{df_drop_na_col}")

#
df_fill_mean = df.fillna(df.mean())
print(df.mean())
print(f"\nЗаполнение пропущенных значений средним значением по столбцу\n{df_fill_mean}")

print(f"Заполнение пропущенных значений постоянным значением\n{df.fillna(0)}\n")



df_dublicates = pd.DataFrame(
    {
        "A": [1, 2, 2, 3, 4, 5],
        "B": [1, 2, 2, 3, 4, 5]
    }
)

print(df_dublicates)
print("Удаление дубликатов\n")
print(df_dublicates.drop_duplicates())

print("\nСоздание DataFrame с типами данных для преобразования\n")
df_types = pd.DataFrame({
    'A': ['1', '2', '3', '4'],
    'B': ['10.1', '20.2', '30.3', '40.4']
})
print(df_types, "\n")
print(df_types.dtypes, "\n")

df_types["A"] = df_types["A"].astype("int")
df_types["B"] = df_types["B"].astype("float")

print("После преобразования\n")
print(df_types, "\n")
print(df_types.dtypes, "\n")


# Создание DataFrame с выбросами
df_outliers = pd.DataFrame({
    'A': [1, 2, 3, 1000, 5]
})
print("Создание DataFrame с выбросами")
print(df_outliers)

df_no_outliers = df_outliers[df_outliers["A"] < 100]
print("\nУдаление выбросов:")
print(df_no_outliers)


# ---------------------  Группировка, агрегация и объединение данных ------------------------


# Пример DataFrame
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'C', 'A', 'C'],
    'Values': [10, 20, 15, 25, 10, 30, 50]
})

print(df, "\n")

group_df = df.groupby("Category", as_index=False).sum()
print("Группировка DataFrame по столбцу 'Category' с суммированием:")
print(group_df)


# Пример Series
s = pd.Series([10, 20, 15, 25, 10, 30], index=['A', 'B', 'A', 'B', 'C', 'A'])
print("\n-------- Series -------------\n")
print(s, "\n")


# Группировка по индексу и вычисление суммы значений в каждой группе
grouped_s = s.groupby(level=0).sum()
print("\nГруппировка Series по индексу с суммированием:")
print(grouped_s, "\n")

agg_df = df\
    .groupby("Category", as_index=False)\
    .agg({"Values": ["sum", "min"]})

print("\nАгрегация DataFrame по столбцу 'Category' с суммой и средним:")
print(agg_df, "\n")

agg_s = s.groupby(level=0).agg(["sum", "mean"])
print("\nАгрегация Series по индексу с суммой и средним:")
print(agg_s, "\n")

# mode() — Находит наиболее часто встречающееся значение в каждой группе.

grouped_mode = df.groupby('Category')['Values'].apply(lambda x: x.mode())
print("\nMode (мода) для каждой категории:")
print(grouped_mode)

# quantile() — Вычисляет определенные квантили для каждой группы. Например, медиана является 50-м процентилем.

grouped_quantile = df.groupby('Category')['Values'].quantile(0.5)
print("\nМедиана (50-й процентиль) для каждой категории:")
print(grouped_quantile)



# Создание двух Series для примера
s1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
s2 = pd.Series([4, 5, 6], index=['A', 'B', 'D'])

print("Исходные Series\n")
print(f"{s1}\n{s2}")

# Объединение Series по строкам (по умолчанию axis=0)
concat_s = pd.concat([s1, s2])
print("\nОбъединение Series по строкам:")
print(concat_s)

# Объединение Series по столбцам (axis=1)
concat_s_axis1 = pd.concat([s1, s2], axis=1)
print("\nОбъединение Series по столбцам:")
print(concat_s_axis1)


# Преобразование Series в DataFrame
df1 = s1.reset_index()
df1.columns = ['Key', 'Value1']

df2 = s2.reset_index()
df2.columns = ['Key', 'Value2']

print(f"{df1}\n{df2}")

# Объединение DataFrame с использованием merge
merged_series_df = pd.merge(df1, df2, on='Key', how='outer')
print("\nОбъединение Series после преобразования в DataFrame:")
print(merged_series_df)

# Дан следующий DataFrame df:
#  Какой код следует использовать для вычисления среднего значения в каждой категории?
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'C', 'A'],
    'Values': [10, 20, 15, 25, 10, 30],
    'Counts': [20, 20, 35, 25, 20, 30]
})
t_1 = df.groupby("Category", as_index=False).mean()
# вариант 2 предпочтительнее
t_1_1 = df.groupby("Category", as_index=False)["Values"].mean()

# Дан следующий DataFrame df:
# df = pd.DataFrame({
#     'Category': ['A', 'B', 'A', 'B', 'C', 'A'],
#     'Values': [10, 20, 15, 25, 10, 30]
# })
# Какой код следует использовать для вычисления разницы между максимальным и минимальным значениями в каждой категории?

t_5 = df.groupby('Category')['Values'].apply(lambda x: x.max() - x.min())
t_5_1 =  df.groupby('Category')['Values'].agg(lambda x: x.max() - x.min())