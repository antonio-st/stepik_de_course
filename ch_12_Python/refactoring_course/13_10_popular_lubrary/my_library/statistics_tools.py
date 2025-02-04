def mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]

def variance(numbers):
    avg = mean(numbers)
    return sum((x - avg) ** 2 for x in numbers) / len(numbers)