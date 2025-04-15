from datetime import datetime
from dao.vehicle_dao import VehicleDAO
from dao.parking_slot_dao import ParkingSlotDAO
from dao.ticket_dao import TicketDAO
from model.vehicle import Vehicle
from model.ticket import Ticket

class ParkingController:

    def enter_parking(self, license_plate, vehicle_type):
        existing_vehicle = VehicleDAO.get_vehicle_by_plate(license_plate)
        if existing_vehicle:
            active_ticket = TicketDAO.get_active_ticket_by_vehicle(existing_vehicle.vehicle_id)
            if active_ticket:
                print("❗ Автомобиль уже на парковке.")
                return

        slot = ParkingSlotDAO.get_available_slot(vehicle_type)
        if not slot:
            print("🚫 Нет свободных мест для типа:", vehicle_type)
            return

        if not existing_vehicle:
            new_vehicle = Vehicle(vehicle_id=None, license_plate=license_plate, vehicle_type=vehicle_type)
            VehicleDAO.add_vehicle(new_vehicle)
            vehicle_id = new_vehicle.vehicle_id
        else:
            vehicle_id = existing_vehicle.vehicle_id

        ticket = Ticket(ticket_id=None, vehicle_id=vehicle_id, slot_id=slot.slot_id)
        TicketDAO.create_ticket(ticket)

        ParkingSlotDAO.update_slot_status(slot.slot_id, True)
        print(f"✅ Авто {license_plate} успешно припарковано на месте #{slot.slot_id}")

    def exit_parking(self, license_plate):
        vehicle = VehicleDAO.get_vehicle_by_plate(license_plate)
        if not vehicle:
            print("🚫 Автомобиль не найден.")
            return

        ticket = TicketDAO.get_active_ticket_by_vehicle(vehicle.vehicle_id)
        if not ticket:
            print("ℹ️ У авто нет активного билета.")
            return

        TicketDAO.close_ticket(ticket.ticket_id)
        ticket.exit_time = datetime.now()

        ParkingSlotDAO.update_slot_status(ticket.slot_id, False)

        duration = ticket.get_duration_minutes()
        price = self.calculate_price(duration)

        print(f"🚗 Авто {license_plate} покинуло парковку.")
        print(f"⏱️ Время: {duration:.2f} минут | 💰 Цена: {price:.2f} сом")

    def calculate_price(self, duration_minutes):
        if duration_minutes is None:
            return 0
        return 10 + (duration_minutes // 15) * 5