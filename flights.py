def add_flight(cursor):
    """
    Adds a new flight to the Flights table.
    """
    print(" please type the information of the new flight ---")
    destination_id = input("type destinationID: ")
    aircraft_id = input("type aircraftID: ")
    pilot_id = input("write PilotID: ")
    departure_time = input("type Departure Time  with the formatYYYY-MM-DD HH:MM:SS: ")
    arrival_time = input("Enter arrival time  with the format YYYY-MM-DD HH:MM:S): ")
    status = input("enter flight Status  possible options: On Time, Delayed: ")

    try:
        cursor.execute("""
            INSERT INTO Flights (DestinationID, AircraftID, PilotID, DepartureTime, ArrivalTime, Status)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (destination_id, aircraft_id, pilot_id, departure_time, arrival_time, status))
        print("flight added successfully!")
    except Exception as e:
        print(f"Error: {e}")

def view_flights_by_criteria(cursor):
    """
    Retrieves flights based on specified criteria.
    """
    print("view Flights by Criteria ---")
    destination_id = input("Enter Destination ID (or press Enter to skip): ")
    status = input("Enter Flight Status (or press Enter to skip): ")
    departure_date = input("Enter Departure Date (YYYY-MM-DD) (or press Enter to skip): ")

    query = "SELECT * FROM Flights WHERE 1=1"
    params = []

    if destination_id:
        query += " AND DestinationID = ?"
        params.append(destination_id)
    if status:
        query += " AND Status = ?"
        params.append(status)
    if departure_date:
        query += " AND DepartureTime >= ? AND DepartureTime < ?"
        params.append(departure_date + " 00:00:00")
        params.append(departure_date + " 23:59:59")

    try:
        cursor.execute(query, params)
        flights = cursor.fetchall()
        if flights:
            print("\n--- Flights Found ---")
            for flight in flights:
                print(flight)
        else:
            print("No flights found matching the criteria.")
    except Exception as e:
        print(f"Error: {e}")

def update_flight(cursor):
    """
    Updates flight information such as departure time or status.
    """
    print("\n--- Update Flight Information ---")
    flight_id = input("Enter Flight ID to update: ")
    new_departure_time = input("Enter new Departure Time (YYYY-MM-DD HH:MM:SS): ")
    new_status = input("Enter new Status (e.g., On Time, Delayed): ")

    try:
        cursor.execute("""
            UPDATE Flights
            SET DepartureTime = ?, Status = ?
            WHERE FlightID = ?;
        """, (new_departure_time, new_status, flight_id))
        print("Flight updated successfully!")
    except Exception as e:
        print(f"Error: {e}")
