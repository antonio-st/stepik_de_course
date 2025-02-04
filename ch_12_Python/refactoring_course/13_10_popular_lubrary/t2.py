# Напишите функцию sin_of_angle(angle: float) -> float, которая принимает угол в градусах и возвращает значение
# синуса этого угла, используя math.radians() и math.sin().
#
# Обязательно округлите результат, используя функцию round.

from math import sin, radians

input_num = int(input())
def sin_of_angle(angle: float) -> float:
    return round(sin(radians(input_num)), 1)

print(sin_of_angle(input_num))