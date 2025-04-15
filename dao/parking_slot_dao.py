from model.db import get_connection
from model.parking_slot import ParkingSlot

class ParkingSlotDAO:
    @staticmethod
    def get_all_slots():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM parking_slots")
            rows = cursor.fetchall()
            return [ParkingSlot(slot_id=row[0], slot_type=row[1], is_occupied=bool(row[2])) for row in rows]

    @staticmethod
    def get_available_slot(slot_type):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM parking_slots WHERE slot_type=? AND is_occupied=0 LIMIT 1", (slot_type,))
            row = cursor.fetchone()
            if row:
                return ParkingSlot(slot_id=row[0], slot_type=row[1], is_occupied=bool(row[2]))
            return None

    @staticmethod
    def update_slot_status(slot_id, is_occupied):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE parking_slots SET is_occupied=? WHERE slot_id=?", (int(is_occupied), slot_id))
            conn.commit()