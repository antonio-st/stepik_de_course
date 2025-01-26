# Напишите программу, которая принимает число и вычисляет сумму его цифр с помощью цикла while.

input_num = input()
len_num = len(input_num)
acc = 0
while len_num > 0:
    len_num -= 1
    acc += int(input_num[len_num - 1])

print(f"Сумма цифр числа {int(input_num)}: {acc}")
