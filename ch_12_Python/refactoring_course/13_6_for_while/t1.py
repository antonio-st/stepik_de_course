# Напишите программу, которая принимает число и проверяет, является ли оно простым.
# Используйте цикл for для проверки делителей числа.

input_num = int(input())
chk_div = 0

for i in range(2, input_num):
    if input_num % i == 0:
        chk_div = 1

if chk_div == 0:
    print(f"Число {input_num} является простым")
else:
    print(f"Число {input_num} не является простым")