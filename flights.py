def add_flight(cursor):
    print("\n--- Add a New Flight ---")
    destination_id = input("Enter Destination ID: ")
    aircraft_id = input("Enter Aircraft ID: ")
    pilot_id = input("Enter Pilot ID: ")
    departure_time = input("Enter Departure Time (YYYY-MM-DD HH:MM:SS): ")
    arrival_time = input("Enter Arrival Time (YYYY-MM-DD HH:MM:SS): ")
    status = input("Enter Flight Status (e.g., On Time, Delayed): ")

    try:
        cursor.execute("""
            INSERT INTO Flights (DestinationID, AircraftID, PilotID, DepartureTime, ArrivalTime, Status)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (destination_id, aircraft_id, pilot_id, departure_time, arrival_time, status))
        print("Flight added successfully!")
    except Exception as e:
        print(f"Error: {e}")
