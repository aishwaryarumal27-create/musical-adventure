import sqlite3
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")
cursor.execute("INSERT INTO interns VALUES (1,'Alice','Data Science',20000)")
cursor.execute("INSERT INTO interns VALUES (2,'Bob','Web Dev',18000)")
cursor.execute("INSERT INTO interns VALUES (3,'Charlie','Data Science',22000)")
cursor.execute("INSERT INTO interns VALUES (4,'David','Cloud Computing',21000)")
cursor.execute("INSERT INTO interns VALUES (5,'Eva','Web Dev',19000)")
conn.commit()
cursor.execute("SELECT name, track FROM interns")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()