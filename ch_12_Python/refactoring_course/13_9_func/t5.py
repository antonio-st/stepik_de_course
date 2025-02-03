# Создайте функцию reverse_numbers(lst: list) -> list, которая принимает список чисел и возвращает новый список,
# в котором каждое число представлено в обратном порядке.

input_list = eval(input())

def reverse_numbers(lst: list) -> list:
    rev_list = []
    for i in range(len(lst)):
        rev_list.append(int(str(lst[i])[::-1]))
    return rev_list

print(reverse_numbers(input_list))


