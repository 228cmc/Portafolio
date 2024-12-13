from  validation import validate_choice, validate_string, validate_number

def add_pilot(cursor):
    """
    adds data to the table pilot.
    For that it request information such as pilot id, first name, last name, license name, seniority, emergency contact among others
    this information is validated with some methods of the module validation that checks if its a number and if it's not empty     """


    pilot_id = validate_number("writeP pilot ID: ")
    first_name = validate_string(" write first name: ")
    last_name = validate_string("write Last Name: ")
    license_number = input("write License Number: ")
    seniority = validate_string("write  years of Seniority: ")
    emergency_contact = validate_number("write emergency Contact: ")
    try:
        
        cursor.execute("""
            INSERT INTO pilot (PilotID, FirstName, LastName, LicenseNumber, Seniority, EmergencyContact)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (pilot_id, first_name, last_name, license_number, seniority, emergency_contact))
        print("the pilot was added")
    except :
        print("Error adding the pilot")


def assign_pilot_to_flight(cursor):


    """
    asigns a pilot to an existing flight, for that  it modifies the method """
    
    print("assign Pilot to Flight ")
    flight_id = validate_number("type flightID to update: ")
    pilot_id = validate_number("enter pilot ID: ")

    try:
        cursor.execute("""
            UPDATE flight
            SET PilotID = ?
            WHERE FlightID = ?;
        """, (pilot_id, flight_id))
        print("pilot assigned successfully!")
    except :
        print("Error assigning the pilot")

def view_pilot_schedule(cursor):
    """
    Retrieves the schedule of flight for a specific pilot.
    """
    pilot_id = validate_number("enter Pilot ID: ")
    print(f"Pilot Schedule of pilot_id:{pilot_id}  ")


    try:
        cursor.execute("""
            SELECT flight.FlightID, destination.City, flight.DepartureTime, flight.ArrivalTime, flight.Status
            FROM flight
            JOIN destination ON flight.DestinationID = destination.DestinationID
            WHERE flight.PilotID = ?;
        """, (pilot_id,))
        flight = cursor.fetchall()
        if flight:
            for flight in flight:
                print(f"flightID: {flight[0]}, destination: {flight[1]}, departure: {flight[2]}, Arrival: {flight[3]}, Status: {flight[4]}")
        else:
            print("no flight assigned to this pilot")
    except :
        print("Error assigning the flight")
        #

def delete_pilot(cursor):
    """
    delete information of a pilot
    """
    print(" write the pilot you want to eliminate")
    pilot_id = validate_number("enter Pilot ID: ")
    try:
        cursor.execute(
            """
            DELETE FROM pilot
            WHERE PilotID = ? ;
        """, (pilot_id,))

        #set empty the flight without pilot
        cursor.execute("UPDATE flight SET PilotID = NULL WHERE PilotID = ?;", (pilot_id,))
        print("was deleted")


    except:
        print(" done")

