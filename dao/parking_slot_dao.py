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
    def get_all_slots_with_vehicles():
        query = """
            SELECT ps.slot_id, ps.slot_type, ps.is_occupied, v.license_plate, v.vehicle_type
            FROM parking_slots ps
            LEFT JOIN tickets t ON ps.slot_id = t.slot_id AND t.exit_time IS NULL
            LEFT JOIN vehicles v ON t.vehicle_id = v.vehicle_id
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return [
                {
                    "slot_id": row[0],
                    "slot_type": row[1],
                    "is_occupied": bool(row[2]),
                    "license_plate": row[3] if row[2] else "Свободно",
                    "vehicle_type": row[4] if row[2] else "-"
                }
                for row in rows
            ]

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
    def get_all_available_slots(slot_type):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM parking_slots WHERE slot_type=? AND is_occupied=0", (slot_type,))
            rows = cursor.fetchall()
            return [ParkingSlot(slot_id=row[0], slot_type=row[1], is_occupied=bool(row[2])) for row in rows]

    @staticmethod
    def update_slot_status(slot_id, is_occupied):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE parking_slots SET is_occupied=? WHERE slot_id=?", (int(is_occupied), slot_id))
            conn.commit()