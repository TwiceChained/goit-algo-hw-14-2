import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT 
    t.teacher_name,
    c.course_name
FROM teachers AS t
JOIN courses AS c ON t.id = c.teacher_id
WHERE t.id = 4;
"""

print(execute_query(sql))
