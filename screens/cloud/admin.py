import sqlite3
import os
global connect
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
db_file = os.path.join(BASE_DIR, "db.sqlite3")
conn = sqlite3.connect(db_file, check_same_thread=False)
connect = conn.cursor()

def create():
    connect.execute("""
    CREATE TABLE IF NOT EXISTS "feedback" (
	    "name"	TEXT,
	    "date"	TEXT,
        "time"  TEXT,
	    "feed"	TEXT

	    
    )
    """)
    conn.commit()
create()


import socket
import threading
import asyncio
FORMAT = 'utf-8'
s = socket.socket()		
print ("Socket successfully created")
port = 12345				
s.bind(('', port))		
print ("socket binded to %s" %(port))
s.listen(5)	
print ("socket is listening")			
c, addr = s.accept()	
print ('Got connection from', addr )


def h():
    data=(c.recv(1024).decode(FORMAT))
    d=data.split(":")
    print(d)

    connect.execute("""INSERT INTO feedback (name,date,time,feed) values (?,?,?,?)""",(d[0],d[1],d[2],d[3]))
    conn.commit()

    
def start():
    while True:
        h()
start()
