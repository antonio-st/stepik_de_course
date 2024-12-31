# Напишите программу, которая использует модуль math для вычисления площади и длины окружности по заданному радиусу.
# Ответ округлить до двух знаков после запятой.
# Предусмотреть возможность введения пользователем отрицательного радиуса, в этом случае вернуть значение 0

from math import pi, pow


def calculate_circle_area(radius):
    """Вычисляет площадь круга по заданному радиусу."""
    if radius > 0:
        return pi * pow(radius, 2)
    elif radius < 0:
        return 0
    elif radius == 0:
        return float(0)


def calculate_circle_circumference(radius):
    """Вычисляет длину окружности по заданному радиусу."""
    if radius > 0:
        return 2 * pi * radius
    elif radius < 0:
        return 0
    elif radius == 0:
        return float(0)


# Ввод радиуса пользователем
radius = float(input())

print(f"Площадь: {round(calculate_circle_area(radius), 2)}")
print(f"Длина окружности: {round(calculate_circle_circumference(radius), 2)}")