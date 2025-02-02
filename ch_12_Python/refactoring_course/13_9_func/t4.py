# Создайте функцию int_to_roman(num: int) -> str, которая переводит целое число (до 3999) в римское представление.

input_num = int(input())

def int_to_roman(num: int) -> str:
    num = list(str(num))
    rome = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
            4: 'IV', 1: 'I'}
    hous_tr = len(num)
    if hous_tr > 3:
        hous_res = rome[1000] * (int(num[0]) % 1000)
    else:
        hous_res = ""

    num_2 = rome[int(num[1]) * 100]
    num_3 = rome[int(num[2]) * 10]
    num_4 = rome[int(num[3])]
    return hous_res + num_2 + num_3 + num_4

print(int_to_roman(input_num))


# решение преподавателя


def int_to_roman(num: int) -> str:
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ""
    for i in range(len(val)):
        count = num // val[i]
        roman += syms[i] * count
        num -= val[i] * count
    return roman

# Вызов функции
result = int_to_roman(3549)
print(result)  # "MMMDXLIX"

