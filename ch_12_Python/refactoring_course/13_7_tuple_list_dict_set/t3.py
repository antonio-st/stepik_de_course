# Дано несколько кортежей, каждый из которых содержит по два элемента (a, b).
# Напишите программу, которая находит кортеж с наибольшей суммой элементов и кортеж с наименьшей суммой элементов.


input_tuple = eval("[" + input("").replace(" ", ",") + "]")
tuple_acc_max = (input_tuple[0])
tuple_acc_min = (input_tuple[0])

for i in range(len(input_tuple)):
    if sum(input_tuple[i]) > sum(tuple_acc_max):
        tuple_acc_max = input_tuple[i]
    elif sum(input_tuple[i]) < sum(tuple_acc_min):
        tuple_acc_min = input_tuple[i]

print(f"Кортеж с наибольшей суммой: {tuple_acc_max}")
print(f"Кортеж с наименьшей суммой: {tuple_acc_min}")

# преподаватель

tuples = eval("[" + input("").replace(" ", ",") + "]")

max_tuple = max(tuples, key=lambda x: x[0] + x[1])
min_tuple = min(tuples, key=lambda x: x[0] + x[1])

print("Кортеж с наибольшей суммой:", max_tuple)
print("Кортеж с наименьшей суммой:", min_tuple)