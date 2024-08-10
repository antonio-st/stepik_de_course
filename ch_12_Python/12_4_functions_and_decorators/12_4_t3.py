# Напишите рекурсивную функцию для вычисления n-го числа Фибоначчи.
#
# Числа Фибоначчи определяются следующим образом: F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) для n > 1.

    def fibonacci(n, memo={}):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
            return memo[n]

print(fibonacci(10))