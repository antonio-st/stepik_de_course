import pandas as pd
import numpy as np

# Какой код следует использовать для удаления всех строк, содержащих хотя бы одно пропущенное значение?
print("task 1\n")
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [10, 11, 12, np.nan]
})

print(df, "\n")
print(df.dropna(),"\n")

# Используя тот же DataFrame df, какой код следует использовать для
# заполнения всех пропущенных значений в столбце 'B' средним значением по этому столбцу?
print("task 2\n")
df["B"].fillna(df["B"].mean(), inplace=True)
print(df)


# Какой код следует использовать для преобразования столбца 'Year' в числовой формат?
df_2 = pd.DataFrame({
    'Year': ['2020', '2021', '2022'],
    'Revenue': ['1000', '2000', '3000']
})
print("\ntask 3\n")

print(df_2, "\n")
# все варианты подходят!!!
# df_2["Year"] = df_2["Year"].astype("int")
# df_2['Year'] = pd.to_numeric(df_2['Year'])
df_2['Year'] = df_2['Year'].apply(int)
print(df_2, "\n")
print(df_2.dtypes)


# Какой код следует использовать для удаления выбросов с использованием межквартильного размаха (IQR)?

s_1 = pd.Series([10, 12, 13, 14, 15, 100, 101, 102])

print("\ntask 4\n")

Q1 = s_1.quantile(0.25)
Q3 = s_1.quantile(0.75)

print(Q1, Q3)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"IQR: {IQR}")
print(f"Нижняя граница выбросов: {lower_bound}")
print(f"Верхняя граница выбросов: {upper_bound}")

s_no_outliers = s_1[(s_1 >= lower_bound) & (s_1 <= upper_bound)]

print(s_no_outliers.tolist())


