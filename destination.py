def manage_destination(cursor):
    """
    Views or updates destination information.
    """
    print("change destination information")
    print("1. view all destination")
    print("2. update a destination")
    choice = input("choose an option: ")

    if choice == "1":
        try:
            cursor.execute("SELECT * FROM destination;")
            destination = cursor.fetchall()
            print("\ndestination")
            for destination in destination:
                print(destination)
        except Exception as e:
            print(f"error: {e}")
    elif choice == "2":
        destination_id = input("type destinationID to uchange: ")
        new_city = input("change new city: ")
        new_country = input("change new country: ")
        new_airport_id = input("change new airport code: ")

        try:
            cursor.execute("""
                UPDATE destination
                SET City = ?, Country = ?, AirportID = ?
                WHERE DestinationID = ?;
            """, (new_city, new_country, new_airport_id, destination_id))
            print("Destination updated successfully!")
        except Exception as e:
            print(f"error: {e}")
    else:
        print("that option is not allowed. exit to main menu.")
