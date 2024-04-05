def finish_me(func):
    def wrapper(text, count):
        for _ in range(count):
            func(text)
    return wrapper


@finish_me
def example(text):
    print(text)


example('print me', count=2)
