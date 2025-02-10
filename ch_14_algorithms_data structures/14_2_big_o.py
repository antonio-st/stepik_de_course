import sys

def example_list(n):
    # Создаем список из n элементов
    lst = [i for i in range(n)]
    return lst

# Размер списка из 1000 элементов
n = int(input("Размер списка -> "))
lst = example_list(n)
print(f"Размер списка из {n} элементов: {sys.getsizeof(lst) / 1024} Кбайт \n {sys.getsizeof(lst) / 1024 / 1024} Мбайт")