import os
from datetime import datetime, timedelta

base_path = os.path.dirname(__file__)

homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_okulik_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def split_line(line):

    parts = line.split(' - ')
    print(parts)

    number_part, date_part = parts[0].split('. ')
    number = number_part.strip()
    date_str = date_part.strip()

    date_format = '%Y-%m-%d %H:%M:%S.%f'
    date = datetime.strptime(date_str, date_format)

    if number == '1':
        new_date = date + timedelta(weeks=1)
        print(f"Начальная дата {date}, дата на неделю позже: {new_date}")

    elif number == '2':
        day_of_week = date.strftime('%A')
        print(f"{date} this was {day_of_week}")

    elif number == '3':
        now = datetime.now()
        days_ago = (now - date).days
        print(f"{date} this date was {days_ago} days ago")


def read_file():
    with open(eugene_okulik_path, 'r', encoding='utf-8') as data_file:
        for line in data_file.readlines():
            yield line.strip()


for data_line in read_file():
    split_line(data_line)
