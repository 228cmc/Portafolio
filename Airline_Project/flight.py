from  validation import validate_choice, validate_string, validate_number

def add_flight(cursor):
    """
    the add flight method allows to insert tada to the flight table by asking the input data. 
    this function use some other methods created in the validation module were if it's an number or string as desired of not
    or if it's part of the list of predetermined choice    """


    #firt we ask for the data to add to the table 
    print(" please type the information of the new flight")
    origin_id = validate_number("type origin ID: ") 
    destination_id = validate_number("type destination ID: ")
    aircraft_id = validate_number("type aircraftID: ")
    pilot_id = validate_number("write PilotID: ")
    departure_time = input("type Departure time  with the formatYYYY-MM-DD HH:MM:SS: ")
    arrival_time = input("Enter arrival time  with the format YYYY-MM-DD HH:MM:S): ")
    status = validate_choice(["On Time", "Delayed"], "enter flight Status  possible options: On Time, Delayed ")

    try:
        #print(f"OriginID: {origin_id}, DestinationID: {destination_id}, AircraftID: {aircraft_id}, PilotID: {pilot_id}, DepartureTime: {departure_time}, ArrivalTime: {arrival_time}, Status: {status}")

        cursor.execute("""
            INSERT INTO flight (OriginID, DestinationID, AircraftID, PilotID, DepartureTime, ArrivalTime, Status)
            VALUES (?, ?, ?, ?, ?, ?, ?);
        """, (origin_id, destination_id, aircraft_id, pilot_id, departure_time, arrival_time, status))  # Ajustado
        print("the flight was added")
    except :
        print("error adding the flight please review the information")



def view_flight_by_criteria(cursor):
    """
    get information about  data from the flight table based on criteria such as FlightID, status, 
    departure time range, or destination.
    """
    print("See flight by criteria")
    print("Leave fields empty if you do not want to filter by that criterion.")

    # Get filter inputs
    flight_id = input("Type Flight ID (or press Enter to skip): ")
    origin_id = input("Type Origin ID (or press Enter to skip): ")  
    destination_id = input("Type Destination ID (or press Enter to skip): ")
    status = input("Enter flight status (On Time, Delayed, or press Enter to skip): ")
    departure_start = input("Type Start of Departure Date Range (YYYY-MM-DD HH:MM:SS) (or press Enter to skip): ")
    departure_end = input("Type End of Departure Date Range (YYYY-MM-DD HH:MM:SS) (or press Enter to skip): ")

    # query per se 
    query = """
        SELECT flight.FlightID, origin.City AS Origin, destination.City AS Destination,
               aircraft.Manufacturer, aircraft.MaximumSpeed, pilot.FirstName, pilot.LastName,
               flight.DepartureTime, flight.ArrivalTime, flight.Status
        FROM flight
        JOIN destination AS origin ON flight.OriginID = origin.DestinationID
        JOIN destination AS destination ON flight.DestinationID = destination.DestinationID
        JOIN aircraft ON flight.AircraftID = aircraft.AircraftID
        JOIN pilot ON flight.PilotID = pilot.PilotID
        WHERE (flight.FlightID = ? OR ? IS NULL)
          AND (flight.OriginID = ? OR ? IS NULL)
          AND (flight.DestinationID = ? OR ? IS NULL)
          AND (flight.Status = ? OR ? IS NULL)
          AND (flight.DepartureTime >= ? OR ? IS NULL)
          AND (flight.DepartureTime <= ? OR ? IS NULL)
    """


    params = [
        flight_id if flight_id else None,
        flight_id if flight_id else None,
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

    # Execute query
    try:
        cursor.execute(query, params)
        flights = cursor.fetchall()

        if flights:
            print("\n- Flights matching the criteria:")
            for flight in flights:
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
            print("No flight found matching the criteria.")
    except Exception as e:
        print(f"Error with the request: {e}")





def update_flight(cursor):
    """
    the method allows to change or modify the dates flight information such as departure time or status.
    """
    print(" Update flightinfo")
    flight_id = validate_number("type FlightID to update: ")
    new_departure_time = input("Enter new Departure Time (YYYY-MM-DD HH:MM:SS): ")
    new_status = input("enter flight Status  possible options: On Time, Delayed ")

    try:
        cursor.execute("""
            UPDATE flight
            SET DepartureTime = ?, Status = ?
            WHERE FlightID = ?;
        """, (new_departure_time, new_status, flight_id))
        print("flight updated")
    except :
        print("error updating the flight")
