# Создайте класс Rectangle, который принимает длину и ширину и позволяет вычислить площадь.

input_len, input_w = int(input()), int(input())
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def square(self):
        return self.length * self.width

rec = Rectangle(input_len, input_w)

print(rec.square())
