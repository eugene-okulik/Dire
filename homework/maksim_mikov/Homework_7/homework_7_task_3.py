str1 = 'результат операции: 42'
str2 = 'результат операции: 54'
str3 = 'результат работы программы: 209'
str4 = 'результат: 2'


def final_sum(strings):
    for string in strings:
        ind = string.index(':') + 1
        print(int(string[ind:]) + 10)


final_sum([str1, str2, str3, str4])
