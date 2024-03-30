def fibonacci_numbers(n):
    result = 0
    next_num = 1
    for i in range(n - 1):
        yield result
        prev = result
        result += next_num
        next_num = prev


count = 1
for number in fibonacci_numbers(100001):
    if count in [5, 200, 1000, 100000]:
        print(number)
    count += 1
    if count > 100000:
        break
