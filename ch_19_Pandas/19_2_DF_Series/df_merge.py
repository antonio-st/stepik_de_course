import pandas as pd
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