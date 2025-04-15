from model.db import get_connection
from model.vehicle import Vehicle

class VehicleDAO:
    @staticmethod
    def add_vehicle(vehicle):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO vehicles (license_plate, vehicle_type) VALUES (?, ?)",
                (vehicle.license_plate, vehicle.vehicle_type)
            )
            conn.commit()
            vehicle.vehicle_id = cursor.lastrowid

    @staticmethod
    def get_vehicle_by_plate(plate):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vehicles WHERE license_plate=?", (plate,))
            row = cursor.fetchone()
            if row:
                return Vehicle(vehicle_id=row[0], license_plate=row[1], vehicle_type=row[2])
            return None