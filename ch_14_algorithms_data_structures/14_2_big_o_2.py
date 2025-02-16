from memory_profiler import profile

# Таким образом, пространственная сложность этого кода будет O(n),
# так как память, которую занимает список, линейно зависит от числа элементов n.
@profile
def example_function(n):
    # Создаем список из n элементов
    lst = [i for i in range(n)]
    return lst

example_function(100000)


# константная пространственную сложность (O(1)),
# Эта функция использует константное количество памяти, поскольку переменная sum_value
# и счетчик i не зависят от размера входных данных n.
@profile
def constant_space(n):
    sum_value = 0  # Используется фиксированная память
    for i in range(n):
        sum_value += i
    return sum_value

constant_space(100000)



# А также рассмотрим квадратичную пространственную сложность.
@profile
def quadratic_space(n):
    matrix = [[0] * n for _ in range(n)]  # Создается двумерный массив n x n
    return matrix

quadratic_space(1000)