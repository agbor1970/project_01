import os
import sqlite3


sqlite_connection = sqlite3.connect('teacher.db')
cursor = sqlite_connection.cursor()

with open('./create_and_insert_tables.sql', 'r') as sqlite_file:
    sql_script = sqlite_file.read()

cursor.executescript(sql_script)
idStudent = input("Введите id студента:")

query = (f"SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name from Students, School where Student_Id = {idStudent} and Students.School_Id = School.School_Id")
cursor.execute(query)

rows = cursor.fetchall()
for row in rows:
    print("ID студента:", row[0])
    print("Имя студента:", row[1])
    print("ID школы:", row[2])
    print("Название школы:", row[3])

cursor.close()
os.remove('teacher.db')