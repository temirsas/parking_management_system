from controller.parking_controller import ParkingController
import os

controller = ParkingController()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    while True:
        print("\n🚘 PARKING MANAGEMENT SYSTEM")
        print("1. Въезд автомобиля")
        print("2. Выезд автомобиля")
        print("3. Просмотр всех мест")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            plate = input("Введите номер авто: ")
            vtype = input("Тип авто (car/bike): ")
            controller.enter_parking(plate, vtype)
        elif choice == "2":
            plate = input("Введите номер авто: ")
            controller.exit_parking(plate)
        elif choice == "3":
            controller.view_all_slots()
        elif choice == "4":
            print("👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор")

if __name__ == "__main__":
    menu()