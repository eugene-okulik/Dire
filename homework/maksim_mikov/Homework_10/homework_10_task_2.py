def finish_me(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper


@finish_me
def example(text, count=1):
    for _ in range(count):
        print(text)


example('print me', count=2)
