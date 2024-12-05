import sqlite3
from flights import add_flight, view_flights_by_criteria, update_flight  #import all the functions that I will use from the differnt modules
from pilots import add_pilot, assign_pilot_to_flight, view_pilot_schedule,delete_pilot
from destinations import manage_destinations

def main():
    connection = sqlite3.connect("flight_management.db")
    cursor = connection.cursor()

    while True:
        print("flight Management System ---")
        print("1. add a new flight")
        print("2. view flights ")
        print("3. update Flights")
        print("4. add pilot")
        print("5. assign pilot to flight")
        print("6. view pilot Schedule")
        print("7. delete information of a pilot")
        print("8. view/Update destination information")
        print("9. quit")
        
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
            delete_pilot(cursor)
        elif choice == "8":
            manage_destinations(cursor)
        elif choice == "9":
            print("exiting...")

            break
        else:
            print(" try again")

        connection.commit()

    connection.close()

if __name__ == "__main__":
    main()

