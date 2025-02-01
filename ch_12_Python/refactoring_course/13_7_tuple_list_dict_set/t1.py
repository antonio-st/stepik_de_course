# Напишите программу, которая находит наиболее часто встречающийся элемент в списке.
# Если таких элементов несколько, выведите любой из них.

input_nums = input().split()
f_dict = {}

for char in input_nums:
    if char in f_dict:
        f_dict[char] += 1
    else:
        f_dict[char] = 1

# for key, value in f_dict.items():
#     if key != " " and value > value_acc:
#         key_acc = key
#         value_acc = value

most_frequent = max(f_dict, key=f_dict.get)
print(f"Наиболее часто встречающийся элемент: {most_frequent}")

# нормальная реализация
# elements = input("").split()
# count_dict = {}
#
# for elem in elements:
#     count_dict[elem] = count_dict.get(elem, 0) + 1
#     print(count_dict)
#
# most_frequent = max(count_dict, key=count_dict.get)
# print("Наиболее часто встречающийся элемент:", most_frequent)
