# Напишите функцию, которая принимает список чисел и возвращает их среднее значение.
# Входные значения: строка состоящая из значений, разделенные запятой
# Выходное значение: среднее значение входных элементов


def avg_list(str_num):
    to_list = str_num.replace(", ", " ").split()
    to_list_float = list(map(float, to_list))
    if len(to_list_float) == 0:
        return 0
    else:
        return sum(to_list_float) / len(to_list_float)

print(avg_list(input()))