#6
# Напишите программу, которая принимает строку и переводит первую букву каждого слова в заглавную.

input_text = input().title()

print(f"Отформатированная строка: {input_text}")


#7
# Напишите программу, которая находит самое длинное слово в строке.

input_string = input()
# разбиваем строку по пробелу -> список
split_str = input_string.split()
# находим макс. объект в списке
max_words = max(split_str, key=len)

print(f"Самое длинное слово: {max_words} ")

#8
# Напишите программу, которая подсчитывает количество гласных и согласных букв в строке.

string = input()

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxz'

# Преобразуем строку в нижний регистр и убираем пробелы
string = string.lower().replace(' ', '')

# сравниваем каждый символ с набором гласных
num_vowels = sum(string.count(v) for v in vowels)
# сравниваем каждый символ с набором согласных
num_consonants = sum(string.count(c) for c in consonants)

print(f"Гласные: {num_vowels}\nСогласные: {num_consonants}")

#9
# Напишите программу, которая принимает строку и выводит слова в обратном порядке.

input_string = input()
# разбиваем слова по пробелу
str_to_list = input_string.split(" ")

# разворачиваем список, преобразуем в строку
list_to_str = " ".join(str_to_list[::-1])

print(f"Обратный порядок слов: {list_to_str}")