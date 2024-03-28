number = 5
while True:
    user_input = int(input('Enter random number: '))
    if user_input == number:
        break
    else:
        print('попробуйте снова')
print('Поздравляю! Вы угадали!')
