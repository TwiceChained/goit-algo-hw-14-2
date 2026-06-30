import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT 
    s.student_name,
    c.course_name,
    ROUND(AVG(g.grade_value), 2) AS average_grade
FROM students AS s 
JOIN grades AS g ON s.id = g.student_id
JOIN courses AS c ON c.id = g.course_id
WHERE c.id = 1
GROUP BY s.id, s.student_name, c.course_name
ORDER BY average_grade DESC
LIMIT 1;
"""

print(execute_query(sql))
