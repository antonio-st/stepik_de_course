def fibonacci(n):
    if n == 0:  # базовый случай
        return 0
    elif n == 1:  # базовый случай
        return 1
    else:  # рекурсивный случай
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

# Мемоизация — это техника оптимизации, при которой результаты вычислений сохраняются, чтобы избежать повторных вычислений.
# В данном примере числа вычисляются один раз для входного n, записываются в словарь и дальше уже берутся из него
# а не вычисляются полностью,
# что значительно уменьшает количество действий
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