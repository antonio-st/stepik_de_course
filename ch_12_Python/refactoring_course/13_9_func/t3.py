# Напишите функцию second_largest(numbers: list) -> int, которая возвращает второе по величине число в списке.
# Предполагается, что в списке содержится не менее двух уникальных чисел.

input_str = input().replace("[", "").replace("]", "")
str_list = list(map(int, input_str.split(",")))

def second_largest(numbers: list) -> int:
    return sorted(numbers, reverse=True)[1]

print(second_largest(str_list))


# вариант 2 с eval
def second_largest(line):
    numbers = sorted(eval(line))
    return numbers[-2]

print(second_largest(input()))
