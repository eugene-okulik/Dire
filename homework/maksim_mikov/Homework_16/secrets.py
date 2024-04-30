import mysql.connector as mysql
# from homework.maksim_mikov.Homework_16 import creds
import os
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)
cursor.execute("SELECT * FROM books WHERE taken_by_student_id = 1110")
print('Все книги, которые находятся у студента', cursor.fetchall())
