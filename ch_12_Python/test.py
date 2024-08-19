# from itertools import groupby
#
# numbers = [["2024-06-21", 5], ["2024-06-22", 10], ["2024-06-22", 15], ["2024-06-21", 20]]
# numbers = [1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5]
#
# groups = []
# for k, g in groupby(numbers, key=lambda x: x):
#     print(k, g)
#     groups.append(list(g))
# print(groups)

# for i in range(0, len(numbers)):
#     print(numbers[i][0])



import pandas as pd

numbers = [["2024-06-21", 5], ["2024-06-22", 10], ["2024-06-22", 15], ["2024-06-21", 20]]

dates = ['2020-01-05', '2020-01-12', '2020-01-19', '2020-01-26', '2020-02-02', '2020-02-09', '2020-02-16', '2020-03-01', '2020-03-08']

# df = pd.DataFrame({'dates': pd.date_range(start='1/1/2020', freq='W', periods=len(dates))})
df = pd.DataFrame(numbers, columns=["date", "sum_sales"])

users_purchases = df.groupby('date', as_index=False) \
    .agg({'sum_sales': 'sum'})
print(users_purchases)