def fibonacci_numbers(n):
    result = 0
    next_num = 1
    for i in range(n - 1):
        prev = result
        result += next_num
        next_num = prev
    return result


print(fibonacci_numbers(5))
print(fibonacci_numbers(200))
print(fibonacci_numbers(1000))
print(fibonacci_numbers(100000))
