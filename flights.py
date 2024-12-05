def add_flight(cursor):
    """
    Adds a new flight to the flight table.
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
            INSERT INTO flight (DestinationID, AircraftID, PilotID, DepartureTime, ArrivalTime, Status)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (destination_id, aircraft_id, pilot_id, departure_time, arrival_time, status))
        print("the flight was added")
    except Exception as e:
        print(f"Error: {e}")



def view_flight_by_criteria(cursor):
    """
    Retrieves flight based on fixed criteria, including status, departure time range, or destination.
    """
    print("\n-see flight by criteria")
    print("Leave fields empty if you do not want to filter by that criterion.")

    # get the data
    destination_id = input("type Destination ID (or press Enter to continue): ")
    status = input("type Flight Status (e.g., On Time, Delayed, or press Enter to continue): ")
    departure_start = input("type Start of Departure Date Range (YYYY-MM-DD HH:MM:SS) (or press Enter to skip): ")
    departure_end = input("type End of Departure Date Range (YYYY-MM-DD HH:MM:SS) (or press Enter to skip): ")

    # query
    query = """
        SELECT flight.FlightID, destination.City, aircraft.Manufacturer, pilot.FirstName, pilot.LastName, 
               flight.DepartureTime, flight.ArrivalTime, flight.Status
        FROM flight
        JOIN destination ON flight.DestinationID = destination.DestinationID
        JOIN aircraft ON flight.AircraftID = aircraft.AircraftID
        JOIN pilot ON flight.PilotID = pilot.PilotID
        WHERE (flight.DestinationID = ? OR ? IS NULL)
          AND (flight.Status = ? OR ? IS NULL)
          AND (flight.DepartureTime >= ? OR ? IS NULL)
          AND (flight.DepartureTime <= ? OR ? IS NULL)
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
        flight = cursor.fetchall()

        if flight:
            print("\n-flight with the criteria")
            for flight in flight:
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
            print("no flight found matching the criteria")
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
            UPDATE flight
            SET DepartureTime = ?, Status = ?
            WHERE FlightID = ?;
        """, (new_departure_time, new_status, flight_id))
        print("flight updated")
    except Exception as e:
        print(f"error: {e}")
