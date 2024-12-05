from  validation import validate_choice, validate_string, validate_number

def add_flight(cursor):
    """
    Adds a new flight to the flight table.
    """


    #firt we ask for the data to add to the table 
    print(" please type the information of the new flight")
    origin_id = validate_number("type Origin ID: ")  
    destination_id = validate_number("type destinationID: ")
    aircraft_id = validate_number("type aircraftID: ")
    pilot_id = validate_number("write PilotID: ")
    departure_time = input("type Departure Time  with the formatYYYY-MM-DD HH:MM:SS: ")
    arrival_time = input("Enter arrival time  with the format YYYY-MM-DD HH:MM:S): ")
    status = input("enter flight Status  possible options: On Time, Delayed: ")

    try:
        cursor.execute("""
            INSERT INTO flight (OriginID, DestinationID, AircraftID, PilotID, DepartureTime, ArrivalTime, Status)
            VALUES (?, ?, ?, ?, ?, ?, ?);
        """, (origin_id, destination_id, aircraft_id, pilot_id, departure_time, arrival_time, status))  # Ajustado
        print("the flight was added")
    except :
        print("Error adding the flight please review the information")



def view_flight_by_criteria(cursor):
    """
    Retrieves flight based on fixed criteria, including status, departure time range, or destination.
    """
    print("see flight by criteria")
    print("Leave fields empty if you do not want to filter by that criterion.")

    # get the data
    origin_id = validate_number(input("type Origin ID (or press Enter to continue): "))  # Nueva entrada
    destination_id = validate_number(input("type Destination ID (or press Enter to continue): "))
    status = validate_number(input("type Flight Status (e.g., On Time, Delayed, or press Enter to continue): "))
    departure_start = input("type Start of Departure Date Range (YYYY-MM-DD HH:MM:SS) (or press Enter to skip): ")
    departure_end = input("type End of Departure Date Range (YYYY-MM-DD HH:MM:SS) (or press Enter to skip): ")

    # query
    query = """
        SELECT flight.FlightID, origin.City AS Origin, destination.City AS Destination,
               aircraft.Manufacturer, aircraft.MaximumSpeed, pilot.FirstName, pilot.LastName,
               flight.DepartureTime, flight.ArrivalTime, flight.Status
        FROM flight
        JOIN destination AS origin ON flight.OriginID = origin.DestinationID
        JOIN destination AS destination ON flight.DestinationID = destination.DestinationID
        JOIN aircraft ON flight.AircraftID = aircraft.AircraftID
        JOIN pilot ON flight.PilotID = pilot.PilotID
        WHERE (flight.OriginID = ? OR ? IS NULL)
          AND (flight.DestinationID = ? OR ? IS NULL)
          AND (flight.Status = ? OR ? IS NULL)
          AND (flight.DepartureTime >= ? OR ? IS NULL)
          AND (flight.DepartureTime <= ? OR ? IS NULL)
    """
    
    # stablish none  as parameters 
    params = [
        origin_id if origin_id else None,
        origin_id if origin_id else None,
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
                Origin: {flight[1]},
                Destination: {flight[2]},
                Aircraft: {flight[3]},
                Speed: {flight[4]} km/h,
                Pilot: {flight[5]} {flight[6]},
                Departure: {flight[7]},
                Arrival: {flight[8]},
                Status: {flight[9]}
                """)
        else:
            print("no flight found matching the criteria")
    except :
        print("Error with the request")




def update_flight(cursor):
    """
    Updates flight information such as departure time or status.
    """
    print(" Update flightinfo")
    flight_id = validate_number(input("type FlightID to update: "))
    new_departure_time = validate_number((input("Enter new Departure Time (YYYY-MM-DD HH:MM:SS): "))
    new_status = input("Enter new Status (On Time, Delayed): ")

    try:
        cursor.execute("""
            UPDATE flight
            SET DepartureTime = ?, Status = ?
            WHERE FlightID = ?;
        """, (new_departure_time, new_status, flight_id))
        print("flight updated")
    except :
        print("error updating the flight")
