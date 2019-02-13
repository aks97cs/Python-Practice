import sqlite3
db = sqlite3.connect("backup.db")
db.execute("create table details(name varchar,roll_no varchar)")
db.commit()