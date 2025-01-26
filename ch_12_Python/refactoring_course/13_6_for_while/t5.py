# Напишите программу, которая принимает число и вычисляет сумму его цифр с помощью цикла while.

num = input()
len_num = len(num)
acc_1 = 0
acc_2 = 0

if len_num == 6:
    for i in range(0, 3):
        acc_1 += int(num[i])
    for j in range(3, 6):
        acc_2 += int(num[j])

if (acc_2 == acc_1):
    print("Билет счастливый")

# другой вариант
number = int(input(""))

first_half_sum = 0
second_half_sum = 0

for i in range(6):
    digit = number % 10
    if i < 3:
        first_half_sum += digit
    else:
        second_half_sum += digit
    number //= 10

if first_half_sum == second_half_sum:
    print("Билет счастливый")
else:
    print("Билет не является счастливым")