import re

string = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero '

split_string = re.findall(r'\w+|[.,]', string)
# print(words_and_punctuation)

transformed_list = []
# Проходим по каждому элементу в списке
for word in split_string:
    # Если элемент является словом, добавляем 'ing'
    if word.isalpha():
        transformed_list.append(word + 'ing')
    # Если элемент является знаком препинания
    else:
        # Добавляем знак препинания к последнему слову без пробела
        transformed_list[-1] += word

# Соединяем обратно в строку
final_string = ' '.join(transformed_list).strip()
print(final_string)
