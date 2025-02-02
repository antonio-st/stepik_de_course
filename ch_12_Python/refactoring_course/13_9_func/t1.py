# Напишите функцию count_vowels_consonants(s: str) -> dict, которая принимает строку и возвращает словарь
# с количеством гласных и согласных.

def count_vowels_consonants(s: str) -> dict:
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxz'
    s = s.lower().replace(" ", "")
    acc_v, acc_c = 0, 0
    for v in vowels:
        acc_v += s.count(v)
    for c in consonants:
        acc_c += s.count(c)
    print({'vowels': acc_v, 'consonants': acc_c})


count_vowels_consonants(input())