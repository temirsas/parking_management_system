import sqlite3

def init_db():
    with open("resources/schema.sql", "r") as f:
        sql = f.read()

    conn = sqlite3.connect("parking.db")
    cursor = conn.cursor()
    cursor.executescript(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("✅ База данных и таблицы успешно созданы.")