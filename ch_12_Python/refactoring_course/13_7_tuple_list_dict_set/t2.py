# Напишите программу, которая принимает строку и подсчитывает, сколько раз каждое слово встречается в предложении.
# Выведите результат в виде словаря, где ключи — слова, а значения — их частота.

input_str = input().split()
input_str.sort()
word_dict = {}

for i in input_str:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1

print(word_dict)


# Вариант пре-ля
sentence = input("")
words = sentence.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

# вариант 3
# Через множество убираем дубликаты, потом с помощью count считает кол-во вхождений и заносим в словарь.
list = input().split()
set_list = set(list)
my_dict = {}
for i in list:
    if i in set_list:
        my_dict[i] = list.count(i)
print(my_dict)