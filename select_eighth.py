import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT 
    t.teacher_name,
    ROUND(AVG(g.grade_value), 2) AS average_grade
FROM teachers AS t
JOIN courses AS c ON c.teacher_id = t.id
JOIN grades AS g ON g.course_id = c.id
WHERE t.id = 3
GROUP BY t.id, t.teacher_name;
"""

print(execute_query(sql))
