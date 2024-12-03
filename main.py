import sqlite3
from flights import add_flight, view_flights_by_criteria, update_flight
from pilots import assign_pilot_to_flight
from destinations import manage_destinations

def main():
    connection = sqlite3.connect("flight_management.db")
    cursor = connection.cursor()

    while True:
        print("\n--- Flight Management System ---")
        print("1. Add a New Flight")
        print("2. View Flights by Criteria")
        print("3. Update Flight Information")
        print("4. Assign Pilot to Flight")
        print("5. View/Update Destination Information")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_flight(cursor)
        elif choice == "2":
            view_flights_by_criteria(cursor)
        elif choice == "3":
            update_flight(cursor)
        elif choice == "4":
            assign_pilot_to_flight(cursor)
        elif choice == "5":
            manage_destinations(cursor)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

        connection.commit()

    connection.close()

if __name__ == "__main__":
    main()
