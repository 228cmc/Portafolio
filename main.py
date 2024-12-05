import sqlite3
from flights import add_flight, view_flights_by_criteria, update_flight
from pilots import assign_pilot_to_flight, view_pilot_schedule
from destinations import manage_destinations

def main():
    connection = sqlite3.connect("flight_management.db")
    cursor = connection.cursor()

    while True:
        print("flight Management System ---")
        print("1. add a new flight")
        print("2. view flights ")
        print("3. update Flights")
        print("4. assign pilot to flight")
        print("5. view pilot Schedule")
        print("6. view/Update destination information")
        print("7. quit")

        choice = input("pick option: ")

        if choice == "1":
            add_flight(cursor)
        elif choice == "2":
            view_flights_by_criteria(cursor)
        elif choice == "3":
            update_flight(cursor)
        elif choice == "4":
            add_pilot(cursor)
        elif choice == "5":
            assign_pilot_to_flight(cursor)
        elif choice == "6":
            view_pilot_schedule(cursor)
        elif choice == "7":
            manage_destinations(cursor)
        elif choice == "8":
            print("exiting...")

            break
        else:
            print(" try again")

        connection.commit()

    connection.close()

if __name__ == "__main__":
    main()

