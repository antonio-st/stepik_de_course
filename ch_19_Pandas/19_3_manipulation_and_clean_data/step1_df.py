import pandas as pd
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