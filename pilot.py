def add_pilot(cursor):
    """
    adds a new pilot to the db 
    """

    pilot_id = input("write PilotID: ")
    pilot_id = input("Enter Pilot ID: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    license_number = input("Enter License Number: ")
    seniority = input("Enter Years of Seniority: ")
    emergency_contact = input("Enter Emergency Contact: ")
    try:
        cursor.execute("""
            INSERT INTO pilot (PilotID, FirstName, LastName, LicenseNumber, Seniority, EmergencyContact)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (pilot_id, first_name, last_name, license_number, seniority, emergency_contact))
        print("the pilot was addded")
    except :
        print("Error")


def assign_pilot_to_flight(cursor):
    """
    Assigns a pilot to an existing flight.
    """
    print("assign Pilot to Flight ")
    flight_id = input("enter Flight ID: ")
    pilot_id = input("enter Pilot ID: ")

    try:
        cursor.execute("""
            UPDATE flight
            SET PilotID = ?
            WHERE FlightID = ?;
        """, (pilot_id, flight_id))
        print("pilot assigned successfully!")
    except :
        print("Error:")

def view_pilot_schedule(cursor):
    """
    Retrieves the schedule of flight for a specific pilot.
    """
    print(" view Pilot Schedule ")
    pilot_id = input("enter Pilot ID: ")

    try:
        cursor.execute("""
            SELECT flight.FlightID, destination.City, flight.DepartureTime, flight.ArrivalTime, flight.Status
            FROM flight
            JOIN destination ON flight.DestinationID = destination.DestinationID
            WHERE flight.PilotID = ?;
        """, (pilot_id,))
        flight = cursor.fetchall()
        if flight:
            print("\ Pilot Schedule ")
            for flight in flight:
                print(f"flightID: {flight[0]}, destination: {flight[1]}, departure: {flight[2]}, Arrival: {flight[3]}, Status: {flight[4]}")
        else:
            print("no flight assigned to this pilot")
    except :
        print("Error")
        #

def delete_pilot(cursor):
    """
    delete information of a pilot
    """
    print(" write the pilot you want to eliminate")
    pilot_id = input("enter Pilot ID: ")
    try:
        cursor.execute(
            """
            DELETE FROM pilot
            WHERE PilotID = ? ;
        """, (pilot_id,))

        #set empty the flight without pilot
        cursor.execute("UPDATE flight SET PilotID = NULL WHERE PilotID = ?;", (pilot_id,))


    except:
        print(" No pilot with that ID")

