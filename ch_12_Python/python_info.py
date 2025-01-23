 
# ======================= строки =============================

print(w_3[1])
print(w_3[6:12])
print(f"{w_3[0:12:2]} | с интервалом 2")
print(w_4[::-1]) # развернуть строку

# считывание данных
num1, num2, num3 = int(input()), int(input()), int(input())
stage1, stage2, stage3 = [int(input()) for _ in range(3)]

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

#  проверка большой буквы
any(1 for i in pass_check if i.isupper() is True)

# проверка чиселки в пароле
is_dig = any(1 for i in pass_check if i.isdigit() is True)

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



any(i < 50 for i in lst)


if len([i for i in hours if i > 90]) >= 1

# сортировка списка
sorted([a, b, c]

# проверка спец символов / двойной цикл в list compr
list_char = ["!", "@", "#", "$", "%", "&", "*"]
chk_char = 1 if [1 for i in pass_check for j in list_char if i in j] else 0