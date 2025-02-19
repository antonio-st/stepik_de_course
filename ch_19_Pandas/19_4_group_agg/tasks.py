import pandas as pd

# --- 1 ---

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

print("t_1\n",t_1)
print("\n",t_1_1, "\n")

# --- 2 ---
# Используя тот же DataFrame df, какой код следует использовать для вычисления суммы и максимального значения в каждой категории?

t_2 = df\
    .groupby("Category", as_index=False)\
    .agg({"Values":["sum", "max"]})

print("t_2\n", t_2)

# --- 3 ---
# У вас есть два DataFrame: df1 и df2.
# Какой код следует использовать, чтобы объединить эти два DataFrame по ключу 'Key' с использованием внешнего соединения (outer join)?

df1 = pd.DataFrame({'Key': ['A', 'B', 'C'], 'Value1': [1, 2, 3]})
df2 = pd.DataFrame({'Key': ['B', 'C', 'D'], 'Value2': [4, 5, 6]})

t_3 = df1.merge(df2, on="Key", how="outer")
print("\nt_3\n", t_3)

# --- 4 ---
# У вас есть две Series: s1 и s2.
# Какой код следует использовать, чтобы объединить эти две Series в DataFrame, используя общий индекс?

s1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
s2 = pd.Series([4, 5, 6], index=['B', 'C', 'D'])

t_4 = pd.concat([s1, s2], axis=1)
print("\nt_4\n", t_4)

# --- 5 ---
# Дан следующий DataFrame df:
# df = pd.DataFrame({
#     'Category': ['A', 'B', 'A', 'B', 'C', 'A'],
#     'Values': [10, 20, 15, 25, 10, 30]
# })
# Какой код следует использовать для вычисления разницы между максимальным и минимальным значениями в каждой категории?

t_5 = df.groupby('Category')['Values'].apply(lambda x: x.max() - x.min())
t_5_1 =  df.groupby('Category')['Values'].agg(lambda x: x.max() - x.min())
print("\nt_5\n", t_5)
print("\n", t_5_1)