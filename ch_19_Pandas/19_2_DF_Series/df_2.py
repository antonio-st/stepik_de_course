import pandas as pd

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
