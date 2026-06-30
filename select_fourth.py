import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT 
    ROUND(AVG(g.grade_value), 2) AS average_grade
FROM grades AS g;
"""

print(execute_query(sql))
