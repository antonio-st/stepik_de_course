# Создайте класс Circle для представления окружности.
#
# Класс должен иметь атрибут radius (радиус) и методы для вычисления площади и длины окружности.
#
# В случае отрицательного радиуса необходимо вернуть значение 0.
#
# Обычные ответы необходимо округлить до 2 знаков после запятой.


from math import pi, pow

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        """Вычисляет площадь окружности."""
        if self.radius < 0:
            return 0
        if self.radius == 0:
            return float(0)
        else:
            return round(pi * pow(self.radius, 2), 2)

    def calculate_circumference(self):
        """Вычисляет длину окружности."""
        if self.radius < 0:
            return 0
        if self.radius == 0:
            return float(0)
        else:
            return round(2 * pi * radius, 2)

# Пример использования
radius = float(input())
circle1 = Circle(radius)
print("Площадь окружности:", circle1.calculate_area())
print("Длина окружности:", circle1.calculate_circumference())