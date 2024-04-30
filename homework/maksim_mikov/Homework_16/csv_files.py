import csv
import os
import mysql.connector as mysql
import dotenv


# Чтение файла
def read_csv_file():
    base_path = os.path.dirname(__file__)
    homework_path = os.path.dirname(os.path.dirname(base_path))
    file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

    with open(file_path, newline='') as csv_file:
        file_data = csv.DictReader(csv_file)
        data_from_csv = []
        for row in file_data:
            data_from_csv.append(row)
    return data_from_csv


# Подключение к БД
def fetch_data_from_db():
    dotenv.load_dotenv()

    db = mysql.connect(
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSW'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME')
    )

    # Запрос из БД
    cursor = db.cursor(dictionary=True)

    query = f'''
    SELECT st.name , st.second_name,
    g.title AS group_title,
    bk.title AS book_title,
    ls.title AS lesson_title,
    sb.title AS subject_title,
    mk.value AS mark_value
    FROM students st
        JOIN `groups` g ON st.group_id = g.id
        LEFT JOIN books bk ON st.id = bk.taken_by_student_id
        LEFT JOIN marks mk ON st.id = mk.student_id
        LEFT JOIN lessons ls ON mk.lesson_id = ls.id
        LEFT JOIN subjets sb ON ls.subject_id = sb.id    
    '''
    cursor.execute(query)
    db_data = cursor.fetchall()
    db.close()
    return db_data


def compare_data(data_from_csv, db_data):
    missing_entries = []
    for el in data_from_csv:
        if el not in db_data:
            missing_entries.append(el)
    return missing_entries


final_data_csv = read_csv_file()
final_db_data = fetch_data_from_db()


missing_data = compare_data(final_data_csv, final_db_data)
if missing_data:
    print("Отсутствующие данные:")
    for entry in missing_data:
        print(entry)
else:
    print("Все данные из файла присутствуют в БД")
