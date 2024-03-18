# Задание 1 - распаковка

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)


# Задание 2

str1 = 'результат операции: 42'

str2 = 'результат операции: 514'

str3 = 'результат работы программы: 9'

ind1 = str1.index('4')
ind2 = str2.index('5')
ind3 = str3.index('9')

print(int(str1[ind1:]) + 10)
print(int(str2[ind2:]) + 10)
print(int(str3[ind3:]) + 10)


# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
surname1, surname2, surname3 = students
subject1, subject2, subject3 = subjects

print(f'Students {surname1}, {surname2}, {surname3} study these subjects: {subject1}, {subject2}, {subject3}')
