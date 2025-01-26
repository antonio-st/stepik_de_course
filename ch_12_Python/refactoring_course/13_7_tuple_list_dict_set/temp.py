# my_set = {1, 2, 3, 4, 5}
# my_set_2 = {3, 4, 5, 6}

# my_set.remove(6) # KeyError: 6 Элемента нет
# my_set.discard(6) # ошибки не будет
# my_set.discard(5) # {1, 2, 3, 4}
# my_set.add(5) # {1, 2, 3, 4, 5}

# print(f"НОД: {max(list(set(acc_1) & set(acc_2)))}")

# print(my_set & my_set_2, my_set | my_set_2, my_set - my_set_2, my_set ^ my_set_2)

# print(list("a", 1, "c"))
# print(("a", 1, "c"))

my_tuple = (1, 2, 3)
my_tuple = (1, 2, 3, 4)
print(my_tuple)