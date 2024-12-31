# Напишите функцию sum_numbers(*args), которая принимает произвольное количество числовых аргументов и возвращает их сумму.

def sum_numbers(*args):
    return sum(list(map(int, args)))

# Разделение входной строки на элементы по пробелу
inp_value = [int(x) for x in input().split()]

# Вывод результатов вычислений
print(sum_numbers(*inp_value))