import sqlite3

bd = sqlite3.connect("2048.sqlite")

cur = bd.cursor()

cur.execute("""
	create table if not exists RECORDS (
	name text,
	score integer
)""")

def best():
	cur.execute("""
	SELECT name gamer, max(score) score from RECORDS
	GROUP by name
	ORDER by score DESC
	limit 3
	""")
	return cur.fetchall()


print(best())
