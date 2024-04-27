import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# Создайте группу (group)
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('Snow_Bars', 'mar 2024', 'may 2024')")
group_id = cursor.lastrowid
print('group_id: ', group_id)
cursor.execute(f"SELECT * FROM `groups` WHERE id = {group_id}")
print(cursor.fetchone())
print('')

# Создайте студента (student) и определите своего студента в группу
cursor.execute(f"INSERT INTO students (name, second_name, group_id) VALUES ('Max', 'Hansen', {group_id})")
student_id = cursor.lastrowid
print('student_id: ', student_id)
cursor.execute(f"SELECT * FROM students WHERE id = {student_id}")
print(cursor.fetchone())
print('')

# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) VALUES ('Ангелы и демоны 2', {student_id})")
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) VALUES ('Происхождение 2', {student_id})")
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) VALUES ('Код Да Винчи 2', {student_id})")

# Создайте несколько учебных предметов (subjects)
cursor.execute("INSERT INTO subjets (title) VALUES ('SQL_subj v.2')")
subject_id_1 = cursor.lastrowid
print('subject_id_1: ', subject_id_1)
cursor.execute("INSERT INTO subjets (title) VALUES ('Python_subj v.2')")
subject_id_2 = cursor.lastrowid
print('subject_id_2: ', subject_id_2)
print('')

# Создайте по два занятия для каждого предмета (lessons)
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Insert 2', {subject_id_1})")
lesson_id_1 = cursor.lastrowid
print('lesson_id_1: ', lesson_id_1)
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Select 2', {subject_id_1})")
lesson_id_2 = cursor.lastrowid
print('lesson_id_2: ', lesson_id_2)
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('Functions 2', {subject_id_2})")
lesson_id_3 = cursor.lastrowid
print('lesson_id_3: ', lesson_id_3)
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('OOP 2', {subject_id_2})")
lesson_id_4 = cursor.lastrowid
print('lesson_id_4: ', lesson_id_4)
print('')

# Поставьте своему студенту оценки (marks) для всех созданных вами занятий
query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
val = [
    ('5', lesson_id_1, student_id),
    ('5', lesson_id_2, student_id),
    ('5', lesson_id_3, student_id),
    ('4+', lesson_id_4, student_id)
]
cursor.executemany(query, val)

# Все оценки студента
cursor.execute(f"SELECT * FROM marks WHERE student_id = {student_id}")
print('Все оценки студента', cursor.fetchall())
print('')

# Все книги, которые находятся у студента
cursor.execute(f"SELECT * FROM books WHERE taken_by_student_id = {student_id}")
print('Все книги, которые находятся у студента', cursor.fetchall())
print('')

# Для вашего студента выведите всё, что о нем есть в базе: группа, книги,
# оценки с названиями занятий и предметов (всё одним запросом с использованием `Join`)
query = f'''
SELECT st.id, st.name , st.second_name, st.group_id,
	g.title AS group_title,
	bk.title AS book_title,
	mk.value AS mark_value,
	ls.title AS lesson_title,
	sb.title AS subject_title
FROM students st
    JOIN `groups` g ON st.group_id = g.id
    LEFT JOIN books bk ON st.id = bk.taken_by_student_id
    LEFT JOIN marks mk ON st.id = mk.student_id
    LEFT JOIN lessons ls ON mk.lesson_id = ls.id
    LEFT JOIN subjets sb ON ls.subject_id = sb.id
WHERE
    st.id = {student_id}
'''
cursor.execute(query)
print('Вся информация о студенте', cursor.fetchall())

db.commit()
db.close()
