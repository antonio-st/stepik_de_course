# Напишите программу, которая считает количество вхождений заданного слова в строке.
#
# Формат следующий.
#
# Введите строку: hello world, hello data
# Введите слово для поиска: hello

input_text = input()

input_search = input()

print(f"Количество вхождений слова 'hello': {input_text.count(input_search)}")


# Напишите программу, которая принимает строку и заменяет все пробелы на символ подчеркивания.

input_string = input().replace(" ", "_")
print(f"Измененная строка: {input_string}")
