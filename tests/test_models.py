import unittest
from model.parking_slot import ParkingSlot
from model.vehicle import Vehicle
from model.ticket import Ticket
from datetime import datetime, timedelta

class TestParkingSystemModels(unittest.TestCase):

    def test_parking_slot(self):
        slot = ParkingSlot(slot_id=1, slot_type="car", is_occupied=False)
        self.assertFalse(slot.is_occupied)
        slot.occupy()
        self.assertTrue(slot.is_occupied)
        slot.free()
        self.assertFalse(slot.is_occupied)

    def test_vehicle(self):
        vehicle = Vehicle(vehicle_id=1, license_plate="B1234ABC", vehicle_type="car")
        self.assertEqual(vehicle.license_plate, "B1234ABC")
        self.assertEqual(vehicle.vehicle_type, "car")

    def test_ticket_duration(self):
        start = datetime.now() - timedelta(minutes=30)
        end = datetime.now()
        ticket = Ticket(ticket_id=1, vehicle_id=1, slot_id=1, entry_time=start, exit_time=end)
        self.assertAlmostEqual(ticket.get_duration_minutes(), 30, delta=1)

    def test_ticket_open_and_close(self):
        ticket = Ticket(ticket_id=2, vehicle_id=2, slot_id=5)
        self.assertIsNone(ticket.exit_time)
        ticket.close_ticket()
        self.assertIsNotNone(ticket.exit_time)

if __name__ == '__main__':
    unittest.main()