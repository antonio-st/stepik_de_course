# Напишите программу, которая считает сумму двух чисел.

input_num = input().split()

res_num = sum(map(int, input_num))

print(res_num)