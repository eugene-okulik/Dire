import random

salary = int(input('Enter random number: '))
bonus = random.choice([True, False])

if bonus:
    print(f'{salary}, {bonus} - ${salary + random.randrange(0, 1000)}')
