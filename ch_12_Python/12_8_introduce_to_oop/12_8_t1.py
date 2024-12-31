# Создайте класс Rectangle для представления прямоугольника.
# Класс должен иметь атрибуты width (ширина) и height (высота), а также методы для вычисления
# площади и периметра прямоугольника.
#
# В случае отрицательных значений ширины или высоты необходимо вернуть значение 0.
# Обычные ответы необходимо округлить до 2 знаков после запятой.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        """Вычисляет площадь прямоугольника."""
        if self.width > 0 and self.height > 0:
            return round(self.width * self.height, 2)
        else:
            return 0

    def calculate_perimeter(self):
        """Вычисляет периметр прямоугольника."""
        if self.width > 0 and self.height > 0:
            return round((self.width + self.height) * 2, 2)
        else:
            return 0

w = int(input())
h = int(input())
rect1 = Rectangle(w, h)
print("Площадь прямоугольника:", rect1.calculate_area())
print("Периметр прямоугольника:", rect1.calculate_perimeter())