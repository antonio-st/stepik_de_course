# Напишите программу которая будет генерировать 4 случайных целых числа, в заданных пользователем границах,
# записывать их в список и выводить этот список в отсортированном по убываю виде.
# Модуль random уже импортирован в формате import random

# Получение ограничений генерации
from random import randint

a = int(input())
b = int(input())

# Получение случайных значений в пределах от a до b
value1 = str(randint(a, b))
value2 = str(randint(a, b))
value3 = str(randint(a, b))
value4 = str(randint(a, b))

# Создание списка значений
value_str = value1 + " " + value2 + " " + value3  + " " + value4
value_list_int = list(map(int, value_str.split()))

# Вывод отсортированного по убыванию списка
print(sorted(value_list_int, reverse=True))