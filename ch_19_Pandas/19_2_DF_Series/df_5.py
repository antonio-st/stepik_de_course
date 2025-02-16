import pandas as pd

# Создание первого объекта Series
points_per_game = pd.Series(
    [27.3, 26.0, 21.5, 16.3],
    index=[201939, 201142, 202691, 202326],
    name='pts_per_game'
)

# Создание второго объекта Series
rebounds_per_game = pd.Series(
    [5.3, 6.4, 3.8, 8.2],
    index=[201939, 201142, 202691, 202326],
    name='reb_per_game'
)
print(rebounds_per_game, "\n")
print(rebounds_per_game, "\n")

print("Объединение двух Series в DataFrame")
# res_merge = pd.merge(points_per_game, rebounds_per_game, on="index", how="inner")
res_merge = pd.concat([points_per_game, rebounds_per_game], axis=1)
print(res_merge)