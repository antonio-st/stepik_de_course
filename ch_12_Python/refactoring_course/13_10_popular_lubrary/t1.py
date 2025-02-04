# Напишите функцию rounded_sqrt(n: int) -> int, которая принимает число n и возвращает его квадратный корень,
# округленный до ближайшего целого,с использованием math.sqrt() и math.floor() или math.ceil().

import math as m
input_num = int(input())
def rounded_sqrt(n: int) -> int:
    chk_rem = (m.sqrt(input_num) % 1) > 0.5
    if chk_rem:
        return m.ceil(m.sqrt(n))
    else:
        return m.floor(m.sqrt(n))

print(rounded_sqrt(input_num))