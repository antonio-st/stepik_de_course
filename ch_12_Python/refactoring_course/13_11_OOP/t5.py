# Создайте класс Point, который принимает координаты x и y, и вычисляет расстояние от начала координат.
# Формулу необходимо загуглить)

from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_origin(self):
        return f"Расстояние от начала координат: {round(sqrt(self.x ** 2 + self.y ** 2), 1)}"

input_x, input_y = int(input()),int(input())
point = Point(input_x, input_y)
print(point.distance_origin())