# Создайте класс Person, который принимает имя и возраст и позволяет получить информацию о человеке.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info_person(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

input_name, input_age = input(), int(input())
person = Person(input_name, input_age)
print(person.info_person())


# можно так

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    def __str__(self):
        return f'Имя: {self.name}, Возраст: {self.age}'

name = input()
age = int(input())
print(Person(name, age))