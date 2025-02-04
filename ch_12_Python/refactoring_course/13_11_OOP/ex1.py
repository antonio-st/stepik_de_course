class Car:
    # Атрибуты объекта
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    # Метод
    def describe(self):
        print(f"Это {self.make} {self.model}, {self.year} года выпуска")

# Создание объектов и вызов метода
car_1 = Car("Toyota", "Corolla", 2020)
car_2 = Car("Honda", "Civik", 2019)

car_1.describe()
car_2.describe()
# Это Toyota Corolla, 2020 года выпуска
# Это Honda Civik, 2019 года выпуска