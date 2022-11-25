CREATE TABLE IF NOT EXISTS School (
School_Id INTEGER NOT NULL PRIMARY KEY, 
School_Name TEXT NOT NULL,
Place_Count INTEGER NOT NULL
);

INSERT INTO School (School_Id, School_Name, Place_Count) VALUES
('1', 'Протон', 200),
('2', 'Преспектива', 300),
('3', 'Спектр', 400),
('4', 'Содружество', 500);

CREATE TABLE IF NOT EXISTS Teacher (
Teacher_Id INTEGER NOT NULL PRIMARY KEY, 
Teacher_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL,
Joining_Date TEXT NOT NULL,
Speciality TEXT NOT NULL,
Salary INTEGER NOT NULL,
Experience INTEGER,
FOREIGN KEY(School_Id) REFERENCES School(School_Id)
);

INSERT INTO Teacher (Teacher_Id, Teacher_Name, School_Id, Joining_Date, Speciality, Salary, Experience)
VALUES
('101', 'Галина', '1', '2021-2-10', 'Физик', '40000', NULL),
('102', 'Мария', '1', '2018-07-23', 'Химик', '20000', NULL), 
('103', 'Ольга', '2', '2022-05-19', 'Информатик', '25000', NULL), 
('104', 'Полина', '2', '2017-12-28', 'Физик ', '28000', NULL), 
('105', 'Лидия', '3', '2015-06-04', 'Информатик', '42000', NULL),
('106', 'Анастасия', '3', '2019-09-11', 'Учитель трудов', '30000', NULL),
('107', 'Ирина', '4', '2020-08-21', 'Информатик', '32000', NULL),
('108', 'Виктория', '4', '2017-10-17', 'Географ', '30000', NULL);

CREATE TABLE IF NOT EXISTS Students (
Student_Id INTEGER NOT NULL PRIMARY KEY, 
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL, 
FOREIGN KEY(School_Id) REFERENCES School(School_Id)
);

INSERT INTO Students (Student_Id, Student_Name, School_Id)
VALUES
('201', 'Иван', '1'),
('202', 'Петр', '2'), 
('203', 'Анастасия', '3'), 
('204', 'Игорь', '4');
