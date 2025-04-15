from datetime import datetime

class Ticket:
    def __init__(self, ticket_id, vehicle_id, slot_id, entry_time=None, exit_time=None):
        self.ticket_id = ticket_id
        self.vehicle_id = vehicle_id
        self.slot_id = slot_id
        self.entry_time = entry_time or datetime.now()
        self.exit_time = exit_time

    def close_ticket(self):
        self.exit_time = datetime.now()

    def get_duration_minutes(self):
        if not self.exit_time:
            return None
        delta = self.exit_time - self.entry_time
        return delta.total_seconds() / 60