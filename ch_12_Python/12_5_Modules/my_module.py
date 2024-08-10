# my_module.py

def factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial(n - 1, n * acc)

pi_custom = 3.14

def foo(n):
    if n > 0:
        print("Привет мир")
    else:
        print("Пока мир")