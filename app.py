import sqlite3

db = sqlite3.connect("fighters.db")
cursor = db.cursor()
sql = "SELECT * FROM fighter;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close