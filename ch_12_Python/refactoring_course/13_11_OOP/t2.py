# Создайте класс Circle, который принимает радиус и вычисляет длину окружности. Используйте значение 3.14,
# а не math.pi.

input_radius = int(input())

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def len_circle(self):
         return 2 * 3.14 * self.radius

l_circle = Circle(input_radius)

print(l_circle.len_circle())
