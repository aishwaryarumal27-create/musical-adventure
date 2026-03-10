import sqlite3
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM interns WHERE track='Data Science' AND stipend > 5000")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()