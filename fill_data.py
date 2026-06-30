import faker
from random import randint
import sqlite3

NUMBER_STUDENTS = 40
NUMBER_TEACHERS = 4
NUMBER_GROUPS = 3
NUMBER_COURSES = 5


def generate_fake_data(number_students, number_teachers, number_groups, number_courses) -> tuple:
    fake_students = []  # тут зберігатимемо студентів
    fake_teachers = []  # тут зберігатимемо вчителів
    fake_groups = []  # тут зберігатимемо групи
    fake_courses = [
    "Mathematics",
    "Physics",
    "History",
    "Geography",
    "Chemistry",
    "English",
    "Computer Science",
    "Biology",
    ]  # тут зберігатимемо предмети

    '''Створюємо об'єкт Faker для генерації випадкових даних'''
    fake_data = faker.Faker()

    # Створимо набір студентів у кількості number_students
    for _ in range(number_students):
        fake_students.append(fake_data.unique.name())

    # Згенеруємо тепер number_teachers кількість вчителів'''
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.unique.name())

    # Та number_groups набір груп
    for i in range(1, number_groups + 1):
        fake_groups.append(f"PZ-{100 + i}")
    
    # Та number_courses набір предметів
    fake_courses = fake_courses[:number_courses]

    return fake_students, fake_teachers, fake_groups, fake_courses


def prepare_data(students, teachers, groups, courses) -> tuple:

    for_groups = []
    # готуємо список груп 
    for group in groups:
        for_groups.append((group, ))

    for_teachers = []
    # готуємо список кортежів імена вчителів
    for teacher in teachers:
        for_teachers.append((teacher, ))

    for_students = []
    # готуємо список кортежів імена студентів
    for student in students:
        for_students.append((student, randint(1, NUMBER_GROUPS)))

    for_courses = []  
    # готуємо список кортежів для таблиці courses
    for course in courses:
        for_courses.append((course, randint(1, NUMBER_TEACHERS)))

    
    fake_data = faker.Faker()

    for_grades = []  
    # готуємо список кортежів для таблиці grades
    for student_id in range(1, NUMBER_STUDENTS + 1):
        for _ in range(randint(10, 20)):
            course_id = randint(1, NUMBER_COURSES)
            grade_value = randint(1, 12)
            time_of_grade = fake_data.date_between(start_date="-1y", end_date="today")

            for_grades.append((student_id, course_id, grade_value, time_of_grade))


    return for_groups, for_students, for_teachers, for_courses, for_grades



def insert_data_to_db(groups, students, teachers, courses, grades) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    with sqlite3.connect('university.db') as con:

        cur = con.cursor()

   
        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""
        cur.executemany(sql_to_groups, groups)


        sql_to_students = """INSERT INTO students(student_name, group_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_students, students)


        sql_to_teachers = """INSERT INTO teachers(teacher_name)
                               VALUES (?)"""
        cur.executemany(sql_to_teachers, teachers)


        sql_to_courses = """INSERT INTO courses(course_name, teacher_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_courses, courses)


        sql_to_grades = """INSERT INTO grades(student_id, course_id, grade_value, time_of_grade)
                              VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_grades, grades)

        # Фіксуємо наші зміни в БД
        con.commit()


if __name__ == "__main__":
    groups, students, teachers, courses, grades = prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_GROUPS, NUMBER_COURSES))

    insert_data_to_db(groups, students, teachers, courses, grades)

