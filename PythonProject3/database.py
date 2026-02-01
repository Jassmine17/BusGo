import sqlite3

def connect():
    return sqlite3.connect("busgo.db")

def create_tables():
    con = connect()
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT,
        username TEXT,
        password TEXT,
        role TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS buses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bus_no TEXT,
        route TEXT,
        time TEXT,
        seats INTEGER,
        price REAL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS tickets(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        passenger TEXT,
        bus_no TEXT,
        seat TEXT,
        status TEXT
    )
    """)

    con.commit()
    con.close()
