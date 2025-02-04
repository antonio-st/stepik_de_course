 
# ======================= строки =============================

# считывание данных
num1, num2, num3 = int(input()), int(input()), int(input())
stage1, stage2, stage3 = [int(input()) for _ in range(3)]

# три ввода в список
results = [int(input()) for _ in range(3)]
values = {int(input()) for i in range(3)}

print(w_3[1])
print(w_3[6:12])
print(f"{w_3[0:12:2]} | с интервалом 2")
print(w_4[::-1]) # развернуть строку


# округление
round(sum(numbers1) / len(numbers1), 1)

# целое деление
3660 // 3600 = 1
125 // 60 = 2
# остаток от деления
3660 % 3600 = 60
3725 % 3600 = 125
3725 % 60 = 5


# замена символов с строке
input_string = input().replace(" ", "")

# длина строки
len(text)

print(f"Верхний регистр: {text.upper()}")
print(f"Нижний регистр: {text.lower()}")


print(f"Количество вхождений слова 'hello': {text.count(text)}")

# разбить строку
text.split("@")

# Метод capitalize() в Python возвращает копию строки, в которой первая буква переведена в верхний регистр
text.capitalize()
# Если нужно сделать заглавными первые буквы всех слов в строке, следует использовать метод title()
text.title()

# самое длинное слово в списке
max(split_str, key=len)

## развернуть список слов
# разбиваем слова по пробелу
str_to_list = input_string.split(" ")
# разворачиваем список, преобразуем в строку
list_to_str = " ".join(str_to_list[::-1])

# список в строку 2
*list_to_str



# ============================ if ===============================

x = 0
if x > 0:
    print("x больше 0")
elif x==0:
    print("x равно 0")
else:
    print("x меньше 0")
    
# Тернарный оператор

status = "Совершеннолетний" if age >= 18 else "Несовершеннолетний"

# AND и OR

x = 7
y = 12
if (x > 5 and x < 10) or y == 12:
    print("Либо x в диапазоне от 5 до 10, либо y равно 12.")


# сортировка списка
sorted([a, b, c]

# ======================= цикл for =============================

for i in range(3, 5):
    print(i)
# обратное направление
for i in range(100,1,-1):
    print(i)

# сумма чисел
sum_total = 0
for i in range(1, 101):
    sum_total += i
print("Сумма чисел от 1 до 100:", sum_total)

# найти символ в строке
string = "abracadabra"
count = 0
for char in string:
    if char == 'a':
        count += 1
print(f"Символ 'a' встречается {count} раз.")

# факториал
n = 5
factorial = 1

for i in range(1, n + 1):
    factorial *= i

# вывести True
any(i < 50 for i in lst)
if len([i for i in hours if i > 90]) >= 1

# проверка спец символов / двойной цикл в list compr
list_char = ["!", "@", "#", "$", "%", "&", "*"]
chk_char = 1 if [1 for i in pass_check for j in list_char if i in j] else 0

#  проверка большой буквы
any(1 for i in pass_check if i.isupper() is True)

# проверка чиселки в пароле
is_dig = any(1 for i in pass_check if i.isdigit() is True)


# ======================= цикл while =============================

while условие:
    # блок кода, который выполняется, пока условие истинно

i = 1
while i <= 5:
    print(i)
    i += 1  # Увеличиваем значение переменной на 1, чтобы избежать бесконечного цикла

secret_number = 7
guess = 0
while guess != secret_number:
    guess = int(input("Угадайте число: "))
    if guess == secret_number:
        print("Вы угадали!")
    else:
        print("Неправильно, попробуйте снова!")

# сумма чисел
input_num = input()
len_num = len(input_num)
acc = 0
while len_num > 0:
    len_num -= 1
    acc += int(input_num[len_num - 1])


# ======================= break, continue и pass =============================

# Оператор break:
#     Что делает: Прерывает выполнение цикла и выходит из него полностью, независимо от того, выполнены ли остальные итерации. Цикл завершается, и управление передаётся следующей строке кода после цикла.
#     Когда использовать: Когда нужно досрочно завершить цикл, если выполнено определённое условие.

for i in range(1, 11):
    if i == 5:
        break  # Прерывает цикл, когда i равно 5
    print(i)

# Оператор continue:
    # Что делает: Пропускает текущую итерацию цикла и переходит к следующей, не завершая весь цикл.
    # Когда использовать: Когда нужно пропустить определённые итерации цикла, но продолжить выполнение остальных.
for i in range(1, 6):
    if i == 3:
        continue  # Пропускает текущую итерацию, когда i равно 3
    print(i)

# Оператор pass:
# Ничего не делает, это просто заглушка. Он нужен для тех случаев, когда по синтаксическим правилам должен быть блок кода,
# но по логике на данном этапе выполнения никакие действия не требуются.
# Это может быть полезно при написании скелета программы или для временной заглушки кода.


# ======================= tuple_list_dict_set =============================




## list (список)

# Изменяемость (mutable): Вы можете изменять список после его создания (добавлять, удалять, изменять элементы).
# Упорядоченность: Порядок элементов сохраняется, и каждый элемент имеет индекс.
# Допускает повторяющиеся элементы: Один и тот же элемент может встречаться в списке несколько раз.
# Индексация: Элементы можно обращаться по индексу, начиная с 0.
# clear(): очищает весь список.
my_list = [1, 2, 3, 4]

# append(): добавляет элемент в конец списка.
# insert(): добавляет элемент по указанному индексу.
# remove(): удаляет первый встречный элемент по значению. Удалит только один раз первый элемент.
# pop(): удаляет элемент по индексу и возвращает его (по умолчанию последний элемент).

my_list.remove(2)       # останется [1, 3, 4]
my_list.pop(1)          # останется [1, 4]
my_list.clear()         # останется []
# изменение элемента
my_list[1] = 25         # [10, 25, 30]
# Длина списка
len(my_list) #3

my_list.append(4)       # [1, 2, 3, 4]
my_list.insert(1, "a")  # [1, "a", 2, 3, 4]

# срезы
print(my_list[1:4]) # Вывод: [2, 3, 4]



## -----------------------------------   set (множество)

# Изменяемая (mutable) неупорядоченная коллекция уникальных элементов.
# Множества не допускают дублирующихся значений и не поддерживают индексацию.
# Множества создаются с помощью фигурных скобок {} или функции set().
# Когда использовать: Когда нужна неупорядоченная коллекция без повторяющихся элементов, например,
# для удаления дубликатов или операций над множествами.
my_set = {1, 2, 3, 3, 4, 5} # Вывод: {1, 2, 3, 4, 5}

my_set = {1, 2, 3, 4, 5}

my_set.remove(6) # KeyError: 6 Элемента нет
my_set.discard(6) # ошибки не будет
my_set.discard(5) # {1, 2, 3, 4}
my_set.add(5) # {1, 2, 3, 4, 5}

# пересечение множеств
# intersection(other_set) или &: возвращает новое множество с элементами, которые присутствуют в обоих множествах.
my_set = {1, 2, 3, 4, 5}
my_set_2 = {3, 4, 5, 6}
my_set & my_set_2 # {3, 4, 5}

# объединение
# union(other_set) или |: возвращает новое множество, содержащее все элементы обоих множеств.

my_set | my_set_2 # {1, 2, 3, 4, 5, 6}

# difference(other_set) или - : возвращает новое множество с элементами, которые присутствуют в первом множестве,
# но отсутствуют во втором.
my_set - my_set_2 # {1, 2}


# symmetric_difference(other_set) или ^: возвращает новое множество с элементами, которые присутствуют в одном из
# множеств, но не в обоих.
my_set ^ my_set_2 # {1, 2, 6}

# дано превратить в list
[1, 3, 4, 5, 0, 2] # string
numbers = sorted(eval(line))



## -----------------------------------  dict (словарь)  -----------------------------------

# Изменяемая (mutable) коллекция пар "ключ-значение". Ключи должны быть уникальными и неизменяемыми
# (например, строка, число или кортеж).
# Словари создаются с помощью фигурных скобок {} или функции dict().

my_dict = {"name": "Alice", "age": 25}
my_dict = dict(name="Alice", age=25, city="New York")
print(my_dict["name"])        # Доступ по ключу, вывод: Alice
my_dict["city"] = "New York"  # Добавление пары ключ-значение
# Если ключ уже существует, его значение будет обновлено.
# Если ключа нет, он будет добавлен.

# Удаление элементов
#     del my_dict[key]: удаляет элемент по ключу.
#     pop(key): удаляет элемент и возвращает его значение.
#     popitem(): удаляет последнюю добавленную пару ключ-значение (актуально для версии Python 3.7+).
#     clear(): удаляет все элементы из словаря.

my_dict = {"a": 1, "b": 2, "c": 3}
my_dict.pop("b")          # Удаляет ключ 'b'
print(my_dict)             # Вывод: {'a': 1, 'c': 3}

# Доступ к значениям
#     Через квадратные скобки my_dict[key].
#     Метод get(key, default): возвращает значение по ключу, если его нет — возвращает значение по умолчанию.
my_dict = {"a": 1, "b": 2}
print(my_dict.get("a"))     # Вывод: 1
print(my_dict.get("z", 0))  # Вывод: 0, так как ключа "z" нет

# Проверка наличия ключа
#     in проверяет, есть ли ключ в словаре.
if "a" in my_dict:
    print("Ключ 'a' есть в словаре")

# Перебор элементов словаря
#     keys(): возвращает все ключи.
#     values(): возвращает все значения.
#     items(): возвращает пары ключ-значение в виде кортежей.
my_dict = {"a": 1, "b": 2, "c": 3}
for key in my_dict.keys():
    print(key)              # Вывод: a b c
for value in my_dict.values():
    print(value)            # Вывод: 1 2 3
for key, value in my_dict.items():
    print(key, value)       # Вывод: a 1, b 2, c 3

text = "hello world"
frequency = {}

# словарь для подсчета частоты элементов.
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)  # Вывод: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# Напишите программу, которая находит наиболее часто встречающийся элемент в списке.
# Если таких элементов несколько, выведите любой из них.
elements = input("").split()
count_dict = {}

for elem in elements:
    count_dict[elem] = count_dict.get(elem, 0) + 1
    print(count_dict)

most_frequent = max(count_dict, key=count_dict.get)
print("Наиболее часто встречающийся элемент:", most_frequent)


# Напишите программу, которая принимает список чисел и создает словарь, в котором ключи — это сами числа,
# # а значения — их квадраты. Выведите только те пары, где квадрат числа чётный
input_num = input().split()
acc_sqr = {}
for i in input_num:
    if (int(i) * int(i)) % 2 == 0:
        acc_sqr[int(i)] = int(i) * int(i)


# Напишите программу, которая принимает строку и подсчитывает, сколько раз каждое слово встречается в предложении.
# Выведите результат в виде словаря, где ключи — слова, а значения — их частота.
sentence = input("")
words = sentence.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)


## ----------------------------- tuple (кортеж) -----------------------------



# Неизменяемая (immutable) упорядоченная коллекция элементов.
# Как и списки, кортежи поддерживают индексацию, но их содержимое нельзя изменять после создания.
# Когда использовать: Когда требуется упорядоченная, но неизменяемая коллекция элементов
# (например, для хранения неизменяемых данных).

# Кортежи создаются с помощью круглых скобок ().
# Создание кортежа с числами
my_tuple = (1, 2, 3)
# Создание кортежа без скобок
my_tuple = 1, 2, 3

my_tuple = (1, )
# взятие элементов так же как в списке с 0 и -1

#
#     Кортежи неизменяемы, поэтому добавить, удалить или изменить элемент нельзя.
#     Если нужно изменить кортеж, можно преобразовать его в список, изменить, а затем вернуть кортеж.

my_tuple = (1, 2, 3)
my_list = list(my_tuple)  # Преобразование в список
my_list[0] = 10
my_tuple = tuple(my_list) # Преобразование обратно в кортеж
print(my_tuple)           # Вывод: (10, 2, 3)

# Кортежи можно объединять (конкатенация) и умножать (повторение).

tuple1 = (1, 2, 3)
tuple2 = (4, 5)
print(tuple1 + tuple2)    # Вывод: (1, 2, 3, 4, 5)
print(tuple1 * 2)         # Вывод: (1, 2, 3, 1, 2, 3)

print(len(my_tuple))      # Длина, вывод: 3

my_tuple = (1, 2, 3)
for item in my_tuple:
    print(item)

# оператор in, чтобы проверить, присутствует ли элемент в кортеже.

my_tuple = (1, 2, 3)
print(2 in my_tuple)     # Вывод: True
print(5 in my_tuple)     # Вывод: False

# можно распаковывать
my_tuple = (1, 2, 3)
a, b, c = my_tuple

# кортежи являются неизменяемыми, поэтому их можно использовать в качестве ключей
# в словарях (в отличие от списков)

location_data = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles"
}
print(location_data[(40.7128, -74.0060)])  # Вывод: New York


# Из особенностей -
#     Неизменяемость: После создания кортеж нельзя изменить — элементы нельзя добавить, удалить или изменить.
#     Упорядоченность: Элементы кортежа хранятся в определённом порядке, и их можно получить по индексу.
#     Допускаются дубликаты: В кортежах могут быть повторяющиеся значения.
#     Разные типы данных: Кортежи могут содержать элементы разных типов (числа, строки, списки и т. д.).

# Дано несколько кортежей, каждый из которых содержит по два элемента (a, b).
# Напишите программу, которая находит кортеж с наибольшей суммой элементов и кортеж с наименьшей суммой элементов.

tuples = eval("[" + input("").replace(" ", ",") + "]")

max_tuple = max(tuples, key=lambda x: x[0] + x[1])
min_tuple = min(tuples, key=lambda x: x[0] + x[1])

print("Кортеж с наибольшей суммой:", max_tuple)
print("Кортеж с наименьшей суммой:", min_tuple)



## массив (array)
# В Python массив (array) — это структура данных, похожая на список (list), которая хранит последовательность элементов
# одного типа (например, только целые числа или только строки). В отличие от списков, массивы более эффективны для
# хранения данных фиксированного типа и предоставляют меньше функциональности, но быстрее обрабатываются, особенно
# при выполнении математических операций.
import array
# Создание массива целых чисел
arr = array.array('i', [1, 2, 3, 4, 5])
# с плавающей запятой
arr_float = array.array('f', [1\.0, 2.0, 3.0, 4.0, 5.0])




# ------------------------------------- try exept files  -------------------------------------

try:
    x = input("Введите число")
    result = 10 / int(x)
    print(f"Результат {result}")
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print(f"Ожидалось число! Получено {x}")
print("Yappiii!!!")


# для чтения
file = open("test.txt", "r")
content = file.read()
print(content)
file.close()

# открыть для записи
file_2 = open("test_2.txt", "w")
file_2.write("Hello Scala from Python")

lines = ["\nLine 1\n", "Line 2\n", "Line 3\n"]
file_2.writelines(lines)
file_2.close()

# дописать в конец
file_2 = open("test_2.txt", "a")
file_2.write("\nHello Python from Scala!")
file_2.close()

# пример
try:
    # Пытаемся открыть и прочитать файл
    with open("data.txt", "r") as file:
        content = file.read()
        print("Содержимое файла:")
        print(content)
except FileNotFoundError:
    # Обработка, если файла нет
    print("Файл не найден. Создаем файл и записываем данные.")
    with open("data.txt", "w") as file:
        file.write("Привет! Это первый текст в файле.")
    print("Файл создан и заполнен.")
except Exception as e:
    # Обработка всех других возможных ошибок
    print("Произошла ошибка:", e)


------------------------------------- популярные библиотеки ---------------------------------

import matplotlib.pyplot as plt

# Построение линейного графика
# Данные
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

z = [1, 2, 3, 4, 5]
o = [14, 12, 10, 8, 6]


plt.plot(x, y, label='Линейный график')
plt.plot(z, o, label='Линейный график')
plt.xlabel('X-ось')
plt.ylabel('Y-ось')
plt.title('Пример линейного графика')
plt.legend()
plt.show()

# Построение гистограммы
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

plt.hist(data, bins=5, color='skyblue', edgecolor='brown')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Пример гистограммы')
plt.show()


# Построение круговой диаграммы
# Данные
labels = ['Яблоки', 'Бананы', 'Вишня', 'Даты']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=200)
plt.title('Круговая диаграмма')
plt.show()


## два графика
# Первый график
x1 = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
# Второй график
x2 = [1, 2, 3, 4]
y2 = [2, 4, 6, 8]
# Построение первого графика
plt.subplot(1, 2, 1)  # 1 строка, 2 столбца, 1 график
plt.plot(x1, y1, 'o-')
plt.title('Квадраты')

# Построение второго графика
plt.subplot(1, 2, 2)  # 1 строка, 2 столбца, 2 график
plt.plot(x2, y2, 's-')
plt.title('Линия')
plt.show()

 # ------------ библиотека -------------

# Структура файлов модуля
# создать папку my_library
# В скрипте math_operations.py содержимое будет следующим.
# 1 файл

# 1 файл
# math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
# 2 файл
# statistics_tools.py
def mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]

def variance(numbers):
    avg = mean(numbers)
    return sum((x - avg) ** 2 for x in numbers)

# 3 файл
# __init__.py
from .math_operations import add, subtract, multiply, divide
from .statistics_tools import mean, median, varian

# импорт и вызов
from my_library import add, mean

print(add(3, 5))         # Вывод: 8
print(mean([1, 2, 3, 4]))  # Вывод: 2.5

## -------------- random --------------

import random
# Генерирует случайное целое число в диапазоне от a до b (включительно).
random.randint(1, 1000)

# Возвращает случайное число с плавающей точкой в диапазоне от 0.0 до 1.0
import random
random.random() #  0.1655714468572238

# Возвращает случайное число с плавающей точкой в диапазоне от a до b. Полезно для более гибкой генерации случайных чисел.
import random
random.uniform(1.0, 10.0)

# Возвращает случайный элемент из последовательности, например, из списка или строки.
colors = ["red", "blue", "green", "yellow"]
color = random.choice(colors)
print(color)  # Например, вывод: blue

# Устанавливает начальное значение для генератора случайных чисел, что позволяет воспроизводить
# те же самые случайные значения при каждом запуске
random.seed(28)
print(random.randint(1, 10))  # Будет одинаковый результат при каждом запуске с этим seed


import string

print(string.digits)
print(string.ascii_letters)
print(string.punctuation)
# 0123456789
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# генерация пароля
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

print(generate_password(12)) # L06l8>5Qo*qW

# орел - решка
import random
def coin():
    list = ["орел", "решка"]
    return random.choice(list)

print(coin())



## --------------------------- math -----------------------


import math

print(math.ceil(5.1)) # округление вверх
print(math.floor(5.9)) # округление вниз
print(math.trunc(5.8)) # отбрасывание дробного
print(math.exp(2))         # Вывод: 7.3890560989306495 (e^2)
print(math.log(8, 2))      # Вывод: 3.0 (логарифм по основанию 2)
print(math.log10(100))     # Вывод: 2.0 (десятичный логарифм)
print(math.pow(2, 3))      # Вывод: 8.0 (2^3)
print(math.sqrt(16))       # Вывод: 4.0 (квадратный корень из 16)
print(math.fabs(-7.5))     # Вывод: 7.5 (модуль числа)
print(math.factorial(5))   # Вывод: 120 (5! = 5 * 4 * 3 * 2 * 1)
print(math.gcd(54, 24))    # Вывод: 6 (наибольший общий делитель 54 и 24)
math.hypot(3, 4) # гипотенуза 5.0

# Напишите функцию sin_of_angle(angle: float) -> float, которая принимает угол в градусах и возвращает
# значение синуса этого угла, используя math.radians() и math.sin().

from math import sin, radians

input_num = int(input())
def sin_of_angle(angle: float) -> float:
    return round(sin(radians(input_num)), 1)

print(sin_of_angle(input_num))




# сумма чисел, функциональный стиль
sum(map(int,nums))

# сумма чисел в списке(список str)
res_num = sum(map(int, input_num))

# groupby группировка одинаковых элементов
x.sort()

for i, j in groupby(x):
    print(i, list(j))