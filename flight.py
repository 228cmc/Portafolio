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
    allows to access or get some specific  data from the flight table based on specific criteria that includes status, departure time range, or destination.
    """
    print("see flight by criteria")
    print("Leave fields empty if you do not want to filter by that criterion.")

    # get the data
    origin_id = input("type Origin ID (or press Enter to continue): ")  
    destination_id = input("type Destination ID (or press Enter to continue): ")
    status = input( "enter flight Status  possible options: On Time, Delayed ")
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
        print("error with the request")




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
