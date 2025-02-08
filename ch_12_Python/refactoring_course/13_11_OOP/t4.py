# Создайте класс Car, который принимает модель и год выпуска и позволяет узнать информацию об автомобиле.

class Car:
    def __init__(self, model, manufactory):
        self.model = model
        self.manufactory = manufactory

    def __str__(self):
        return f"Модель: {self.model}, Год выпуска: {self.manufactory}"

input_model, input_manufactory = input(), int(input())
car = Car(input_model, input_manufactory)
print(car)
