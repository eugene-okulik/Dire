def operation_func(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        elif first == second:
            operation = '+'
        else:
            raise ValueError("Неизвестная ошибка операции")
        return func(first, second, operation)

    return wrapper


@operation_func
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


num1 = int(input('Enter random number: '))
num2 = int(input('Enter random number: '))

result = calc(num1, num2)
print(result)
