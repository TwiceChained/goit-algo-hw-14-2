import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT DISTINCT
    s.student_name,
    c.course_name
FROM students AS s
JOIN grades AS g ON g.student_id = s.id
JOIN courses AS c ON g.course_id = c.id
WHERE s.id = 1
ORDER BY c.course_name;
"""

print(execute_query(sql))
