# Напишите программу, которая принимает на вход две строки и выводит все общие буквы в алфавитном порядке.
# Если общих букв нет, программа должна вывести "Общих букв нет".

str_1, str_2 = list(input()), list(input())
set_int = list(set(str_1).intersection(str_2))

print(f"Общие буквы: {sorted(set_int)[0]}, {sorted(set_int)[1]}")

