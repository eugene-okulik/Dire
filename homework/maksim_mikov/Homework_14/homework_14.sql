--- Создайте студента (student)

    INSERT INTO students (name, second_name, group_id) VALUES ('Mark', 'Hans', 1015)

--- Создайте несколько книг (books) и укажите, что ваш созданный студент взял их

    INSERT INTO** books (title, taken_by_student_id) VALUES ('Ангелы и демоны', 1104)

    INSERT INTO** books (title, taken_by_student_id) VALUES ('Происхождение', 1104)

    INSERT INTO** books (title, taken_by_student_id) VALUES ('Код Да Винчи', 1104)

--- Создайте группу (group) и определите своего студента туда

    INSERT INTO `groups`  (title, start_date, end_date) VALUES ('Bars', 'feb 2024', 'may 2024')

--- Создайте несколько учебных предметов (subjects)

    INSERT INTO subjets (title) VALUES ('SQL_subj')

    INSERT INTO subjets (title) VALUES ('Python_subj')

--- Создайте по два занятия для каждого предмета (lessons)

    INSERT INTO lessons (title, subject_id) VALUES ('Insert', 1439)

    INSERT INTO lessons (title, subject_id) VALUES ('Select', 1439)

    INSERT INTO lessons (title, subject_id) VALUES ('Functions', 1440)

    INSERT INTO lessons (title, subject_id) VALUES ('OOP', 1440)

--- Поставьте своему студенту оценки (marks) для всех созданных вами занятий

    INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', 3536, 1104)

    INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', 3537, 1104)

    INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', 3538, 1104)

    INSERT INTO marks (value, lesson_id, student_id) VALUES ('4+', 3539, 1104)


--Получите информацию из базы данных:

--- Все оценки студента

    SELECT value FROM marks WHERE student_id = 1104

--- Все книги, которые находятся у студента

    SELECT title FROM books WHERE taken_by_student_id =1104

--- Для вашего студента выведите всё, что о нем есть в базе: группа, книги,
--   оценки с названиями занятий и предметов (всё одним запросом с использованием `Join`)

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
    st.id = 1104;