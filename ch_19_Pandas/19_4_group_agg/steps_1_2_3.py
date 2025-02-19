import pandas as pd

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