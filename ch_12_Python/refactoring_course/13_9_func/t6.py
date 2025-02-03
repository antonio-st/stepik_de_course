# Создайте функцию count_divisors(n: int) -> int, которая возвращает количество делителей числа n.

input_num = int(input())

def count_divisors(num: int) -> int:
    return sum([1 for i in range(1, num + 1) if num % i == 0])

print(count_divisors(input_num))