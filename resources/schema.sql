CREATE TABLE IF NOT EXISTS parking_slots (
    slot_id INTEGER PRIMARY KEY AUTOINCREMENT,
    slot_type TEXT NOT NULL,
    is_occupied INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    license_plate TEXT UNIQUE NOT NULL,
    vehicle_type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tickets (
    ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id INTEGER,
    slot_id INTEGER,
    entry_time TEXT,
    exit_time TEXT,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    FOREIGN KEY (slot_id) REFERENCES parking_slots(slot_id)
);