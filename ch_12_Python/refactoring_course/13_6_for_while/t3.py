num_1, num_2 = int(input()), int(input())

div_1 = num_1
div_2 = num_1
acc_1 = []
acc_2 = []

# находим делители числа 1 и записываем в список
while div_1 > 0:
    if div_1 > 0 and (num_1 % div_1) == 0:
        acc_1.append(div_1)
    div_1 -= 1

# находим делители числа 2 и записываем в список
while div_2 > 0:
    if div_2 > 0 and (num_2 % div_2) == 0:
        acc_2.append(div_2)
    div_2 -= 1

# находим пересечения списков и выводим max это и будет НОД
print(f"НОД: {max(list(set(acc_1) & set(acc_2)))}")


# вариант проще
nums = [int(input()) for _ in range(2)]
a, b = max(nums), min(nums)
while b:
    a, b = b, a%b
print(f'НОД: {a}')