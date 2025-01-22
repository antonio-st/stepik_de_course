# Напишите программу, которая принимает email и выводит домен этого email.

input_email = input().split("@")

print(f"Домен: {input_email[1]}")