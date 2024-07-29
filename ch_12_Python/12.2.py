magic_of_real = True

if magic_of_real:
    print("Time to learn some spells!")
else:
    print("Please, try again")

# Основные арифметические операторы:
print("Основные арифметические операторы:")
a = 5 / 3
print(a)
b = 5 // 3
print(b)
c = 5 % 3
print(c)
d = 5 ** 3
print(d)

# Основные операторы сравнения:
print("Основные операторы сравнения:")

print(5 == 3)
print(5 != 3)
print(5 > 3)
print(5 < 3)

# Функция input()
print("Функция input()")

# name = input("Your name -> ")
# print(f"Hello, {name} !")

# Основы условных операторов
print("Основы условных операторов")

weather = "Пасмурно"

if weather.lower() == "дождь":
    print("Возьми зонт")
elif weather.lower() == "солнечно":
    print("Не забудьте солнцезащитные очки")
else:
    print("Хорошего дня!")

print("Цикл For")

my_list = {"a", "b", "end", "begin", "a"}

for i in my_list:
    print(i)

print("Цикл While")

count = 0

while count <= 5:
    print(f"Итерация {count}")
    count += 1

print("Работа с break и continue")

for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("Вывод четных чисел")

for i in range(1, 15):
    if i % 2 == 0:
        print(f"Четное число -> {i}")


