# Напишите функцию hypotenuse(a: float, b: float) -> float, которая возвращает длину гипотенузы прямоугольного
# треугольника с катетами a и b, используя math.hypot().

from math import hypot

input_str = input().replace(",", "").split()

def hypotenuse(a: float, b: float) -> float:
    return hypot(a, b)

print(hypotenuse(int(input_str[0]), int(input_str[1])))
