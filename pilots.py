def add_pilot(cursor):
    """
    adds a new pilot to the db 
    """

    pilot_id = input("write PilotID: ")
    first_name = input("write firstName: ")
    license_number = input("type LicenseNumber: ")
    seniority = input("type seniority ")
    emergency_contact = input("type EmergencyContact ")
    try:
        cursor.execute("""
            INSERT INTO Pilots (PilotID, FirstName, LastName, LicenseNumber, Seniority, Status)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (pilot_id, first_name, license_number, seniority, emergency_contact))
        print("the pilot was addded")
    except Exception as e:
        print(f"Error: {e}")


def assign_pilot_to_flight(cursor):
    """
    Assigns a pilot to an existing flight.
    """
    print("assign Pilot to Flight ---")
    flight_id = input("enter Flight ID: ")
    pilot_id = input("enter Pilot ID: ")

    try:
        cursor.execute("""
            UPDATE Flights
            SET PilotID = ?
            WHERE FlightID = ?;
        """, (pilot_id, flight_id))
        print("pilot assigned successfully!")
    except Exception as e:
        print(f"Error: {e}")

def view_pilot_schedule(cursor):
    """
    Retrieves the schedule of flights for a specific pilot.
    """
    print(" view Pilot Schedule ---")
    pilot_id = input("enter Pilot ID: ")

    try:
        cursor.execute("""
            SELECT Flights.FlightID, Destinations.City, Flights.DepartureTime, Flights.ArrivalTime, Flights.Status
            FROM Flights
            JOIN Destinations ON Flights.DestinationID = Destinations.DestinationID
            WHERE Flights.PilotID = ?;
        """, (pilot_id,))
        flights = cursor.fetchall()
        if flights:
            print("\ Pilot Schedule ---")
            for flight in flights:
                print(f"flightID: {flight[0]}, destination: {flight[1]}, departure: {flight[2]}, Arrival: {flight[3]}, Status: {flight[4]}")
        else:
            print("no flights assigned to this pilot")
    except Exception as e:
        print(f"Error: {e}")
