def add_flight(cursor):
    """
    Adds a new flight to the Flights table.
    """


    #firt we ask for the data to add to the table 
    print(" please type the information of the new flight")
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
    Retrieves flights based on fixed criteria, including status, departure time range, or destination.
    """
    print("\n-see flights by criteria")
    print("Leave fields empty if you do not want to filter by that criterion.")

    # get the data
    destination_id = input("type Destination ID (or press Enter to continue): ")
    status = input("type Flight Status (e.g., On Time, Delayed, or press Enter to continue): ")
    departure_start = input("type Start of Departure Date Range (YYYY-MM-DD HH:MM:SS) (or press Enter to skip): ")
    departure_end = input("type End of Departure Date Range (YYYY-MM-DD HH:MM:SS) (or press Enter to skip): ")

    # query
    query = """
        SELECT Flights.FlightID, Destinations.City, Aircrafts.Manufacturer, Pilots.FirstName, Pilots.LastName, 
               Flights.DepartureTime, Flights.ArrivalTime, Flights.Status
        FROM Flights
        JOIN Destinations ON Flights.DestinationID = Destinations.DestinationID
        JOIN Aircrafts ON Flights.AircraftID = Aircrafts.AircraftID
        JOIN Pilots ON Flights.PilotID = Pilots.PilotID
        WHERE (Flights.DestinationID = ? OR ? IS NULL)
          AND (Flights.Status = ? OR ? IS NULL)
          AND (Flights.DepartureTime >= ? OR ? IS NULL)
          AND (Flights.DepartureTime <= ? OR ? IS NULL)
    """
    
    # stablish none  as parameters 
    params = [
        destination_id if destination_id else None,
        destination_id if destination_id else None,
        status if status else None,
        status if status else None,
        departure_start if departure_start else None,
        departure_start if departure_start else None,
        departure_end if departure_end else None,
        departure_end if departure_end else None,
    ]

    # Ejecutar consulta
    try:
        cursor.execute(query, params)
        flights = cursor.fetchall()

        if flights:
            print("\n--- Flights Matching Criteria ---")
            for flight in flights:
                print(f"""
                FlightID: {flight[0]},
                Destination: {flight[1]},
                Aircraft: {flight[2]},
                Pilot: {flight[3]} {flight[4]},
                Departure: {flight[5]},
                Arrival: {flight[6]},
                Status: {flight[7]}
                """)
        else:
            print("No flights found matching the criteria.")
    except Exception as e:
        print(f"Error: {e}")




def update_flight(cursor):
    """
    Updates flight information such as departure time or status.
    """
    print(" Update flightinfo")
    flight_id = input("type FlightID to update: ")
    new_departure_time = input("Enter new Departure Time (YYYY-MM-DD HH:MM:SS): ")
    new_status = input("Enter new Status (On Time, Delayed): ")

    try:
        cursor.execute("""
            UPDATE Flights
            SET DepartureTime = ?, Status = ?
            WHERE FlightID = ?;
        """, (new_departure_time, new_status, flight_id))
        print("flights updated")
    except Exception as e:
        print(f"error: {e}")
