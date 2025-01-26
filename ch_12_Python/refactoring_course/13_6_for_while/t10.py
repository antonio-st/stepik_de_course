# Напишите программу, которая принимает на вход целое число и находит наибольшую непрерывную
# последовательность одинаковых цифр. Программа должна выводить цифру и длину этой последовательности.
# Используйте только if-else и while (без строк, списков и функций обработки строк).

from itertools import groupby

input_num = input()
seq = list(input_num)

acc_dig = 0
acc_len = 0
acc_res = []
temp = 0
seq.sort()

for i, j in groupby(seq):
     temp = len(list(j))
     if temp > acc_len:
          acc_len = temp
          acc_res = list((int(i), temp))

print(f"Цифра: {acc_res[0]}, Длина последовательности: {acc_res[1]}")