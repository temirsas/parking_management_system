class ParkingSlot:
    def __init__(self, slot_id, slot_type, is_occupied=False):
        self.slot_id = slot_id
        self.slot_type = slot_type  # e.g., "car", "bike"
        self.is_occupied = is_occupied

    def occupy(self):
        self.is_occupied = True

    def free(self):
        self.is_occupied = False