from model.db import get_connection
from model.ticket import Ticket
from datetime import datetime

class TicketDAO:
    @staticmethod
    def create_ticket(ticket):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tickets (vehicle_id, slot_id, entry_time) VALUES (?, ?, ?)",
                (ticket.vehicle_id, ticket.slot_id, ticket.entry_time.isoformat())
            )
            conn.commit()
            ticket.ticket_id = cursor.lastrowid

    @staticmethod
    def close_ticket(ticket_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            now = datetime.now().isoformat()
            cursor.execute("UPDATE tickets SET exit_time=? WHERE ticket_id=?", (now, ticket_id))
            conn.commit()

    @staticmethod
    def get_active_ticket_by_vehicle(vehicle_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tickets WHERE vehicle_id=? AND exit_time IS NULL", (vehicle_id,))
            row = cursor.fetchone()
            if row:
                entry = datetime.fromisoformat(row[3])
                return Ticket(ticket_id=row[0], vehicle_id=row[1], slot_id=row[2], entry_time=entry)
            return None