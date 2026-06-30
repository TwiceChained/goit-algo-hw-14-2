import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT 
    gr.group_name,
    s.student_name
FROM students AS s 
JOIN groups AS gr ON s.group_id = gr.id
WHERE gr.id = 2;
"""

print(execute_query(sql))
