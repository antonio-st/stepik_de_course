# Цифровой корень числа — это результат последовательного сложения его цифр до тех пор, пока не останется одна цифра.
# Напишите программу, которая находит цифровой корень заданного числа.

num = int(input())

# считать сумму до тех пор, пока она не станет 10
while num >= 10:
    num = sum(int(digit) for digit in str(num))

print(f"Цифровой корень: {num}")


# аналог

s = input()
ans = 0
while len(s) > 1:
    ans = sum(map(int, s))
    s = str(ans)