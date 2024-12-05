def assign_pilot_to_flight(cursor):
    """
    Assigns a pilot to an existing flight.
    """
    print("Assign Pilot to Flight ---")
    flight_id = input("Enter Flight ID: ")
    pilot_id = input("Enter Pilot ID: ")

    try:
        cursor.execute("""
            UPDATE Flights
            SET PilotID = ?
            WHERE FlightID = ?;
        """, (pilot_id, flight_id))
        print("Pilot assigned successfully!")
    except Exception as e:
        print(f"Error: {e}")

def view_pilot_schedule(cursor):
    """
    Retrieves the schedule of flights for a specific pilot.
    """
    print(" View Pilot Schedule ---")
    pilot_id = input("Enter Pilot ID: ")

    try:
        cursor.execute("""
            SELECT Flights.FlightID, Destinations.City, Flights.DepartureTime, Flights.ArrivalTime, Flights.Status
            FROM Flights
            JOIN Destinations ON Flights.DestinationID = Destinations.DestinationID
            WHERE Flights.PilotID = ?;
        """, (pilot_id,))
        flights = cursor.fetchall()
        if flights:
            print("\n--- Pilot Schedule ---")
            for flight in flights:
                print(f"FlightID: {flight[0]}, Destination: {flight[1]}, Departure: {flight[2]}, Arrival: {flight[3]}, Status: {flight[4]}")
        else:
            print("No flights assigned to this pilot.")
    except Exception as e:
        print(f"Error: {e}")
