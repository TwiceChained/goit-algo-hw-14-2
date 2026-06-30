import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT 
    gr.group_name,
    c.course_name,
    s.student_name,
    g.grade_value,
    g.time_of_grade
FROM groups AS gr
JOIN students AS s ON s.group_id = gr.id
JOIN grades AS g ON g.student_id = s.id
JOIN courses AS c ON g.course_id = c.id
WHERE gr.id = 1
  AND c.id = 2
ORDER BY s.student_name, g.time_of_grade;
"""

print(execute_query(sql))
