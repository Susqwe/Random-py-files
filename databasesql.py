import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS table1 (
	title TEXT,
	link TEXT
	)""")

db.commit()

titledb = input('title: ')
titlelink = input('link: ')

sql.execute(f"SELECT title FROM table1 WHERE title = '{titledb}'")

if sql.fetchone() is None:
	sql.execute(f"INSERT INTO table1 VALUES (?, ?)", (titledb, titlelink))
	db.commit()
	print("Зарегестрировано")
else:
	print("такая запись уже есть")
	for value in sql.execute("SELECT * FROM table1"):
		print(value)
