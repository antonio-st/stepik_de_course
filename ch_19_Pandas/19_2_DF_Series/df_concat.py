import pandas as pd

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