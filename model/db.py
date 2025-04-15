import sqlite3

DB_NAME = "parking.db"

def get_connection():
    return sqlite3.connect(DB_NAME)