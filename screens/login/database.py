import os
import sqlite3
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
db_file = os.path.join(BASE_DIR, "db.sqlite3")
conn = sqlite3.connect(db_file, check_same_thread=False)
c = conn.cursor()

def creating_table():
        c.execute("""
    CREATE TABLE IF NOT EXISTS "register" (
	    "name"	TEXT,
	    "password"	TEXT
	    
    )
    """)
creating_table()

