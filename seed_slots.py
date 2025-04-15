import sqlite3

def seed_parking_slots():
    conn = sqlite3.connect("parking.db")
    cursor = conn.cursor()

    # Добавим 5 мест для "car" и 3 для "bike"
    for _ in range(5):
        cursor.execute("INSERT INTO parking_slots (slot_type, is_occupied) VALUES (?, ?)", ("car", 0))
    for _ in range(3):
        cursor.execute("INSERT INTO parking_slots (slot_type, is_occupied) VALUES (?, ?)", ("bike", 0))

    conn.commit()
    conn.close()
    print("✅ Парковочные места успешно добавлены.")

if __name__ == "__main__":
    seed_parking_slots()