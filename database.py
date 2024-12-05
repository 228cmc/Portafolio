import sqlite3

def is_table_empty(cursor, table_name):
    """
    Checks if a given table is empty.
    """
    cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
    count = cursor.fetchone()[0]
    return count == 0

def create_tables():
    """
    Creates the necessary tables in the flight_management.db database.
    Exits if tables already exist and contain data.

    The tables created are:

    1. **destination**:
        - Columns: DestinationID, City, Country, AirportID.

    2. **aircraft**:
        - Columns: AircraftID, FuelNeed, Manufacturer, CapacityPersons.

    3. **pilot**:
        - Columns: PilotID, FirstName, LastName, LicenseNumber, Seniority, EmergencyContact.

    4. **flight**:
        - Columns: FlightID, DestinationID, AircraftID, PilotID, DepartureTime, ArrivalTime, Status.
    """
    connection = sqlite3.connect("flight_management.db")
    cursor = connection.cursor()

    # we verify  if there are existing tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    existing_tables = cursor.fetchall()
    if existing_tables:
        print("exiting... there is already data")
        connection.close()
        return

    # Create table destination
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS destination (
        DestinationID INTEGER PRIMARY KEY,
        City TEXT NOT NULL,
        Country TEXT NOT NULL,
        AirportID TEXT NOT NULL
    );
    """)

    # crear tabla aircraft
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS aircraft (
        AircraftID INTEGER PRIMARY KEY,
        FuelNeed REAL NOT NULL,
        Manufacturer TEXT NOT NULL,
        CapacityPersons INTEGER NOT NULL
    );
    """)

    # create table pilot
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pilot (
        PilotID INTEGER PRIMARY KEY,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        LicenseNumber TEXT NOT NULL,
        Seniority INTEGER NOT NULL,
        EmergencyContact TEXT NOT NULL
    );
    """)

    # Crear tabla flight
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS flight (
        FlightID INTEGER PRIMARY KEY,
        DestinationID INTEGER NOT NULL,
        AircraftID INTEGER NOT NULL,
        PilotID INTEGER NOT NULL,
        DepartureTime DATETIME NOT NULL,
        ArrivalTime DATETIME NOT NULL,
        Status TEXT NOT NULL,
        FOREIGN KEY (DestinationID) REFERENCES destination(DestinationID),
        FOREIGN KEY (AircraftID) REFERENCES aircraft(AircraftID),
        FOREIGN KEY (PilotID) REFERENCES pilot(PilotID)
    );
    """)

    connection.commit()
    connection.close()
    print("tables were created")


def view_tables_and_content():
    """
    Displays the names of all tables in the database and their content.
    """
    connection = sqlite3.connect("flight_management.db")
    cursor = connection.cursor()

    try:
        # Obtener el nombre de todas las tablas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if not tables:
            print("no tables")
            return

        print("-tables in the database:")
        for table in tables:
            table_name = table[0]
            print(f"table: {table_name}")

            # Mostrar contenido de cada tabla
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()

            if rows:
                for row in rows:
                    print(row)
            else:
                print("table empty")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        connection.close()


def populate_tables():
    """
    Populates the tables with sample data for testing.
    Exits if tables already contain data.
    """
    connection = sqlite3.connect("flight_management.db")
    cursor = connection.cursor()

    # Verificar si ya hay datos en una tabla clave (e.g., destination)
    if not is_table_empty(cursor, "destination"):
        print("exiting... tables were already populated")
        connection.close()
        return

    # Insertar datos en destination
    cursor.executemany("""
    INSERT INTO destination (DestinationID, City, Country, AirportID)
    VALUES (?, ?, ?, ?);
    """, [
        (1, 'Bogotá', 'Colombia', 'BOG'),
        (2, 'Lima', 'Perú', 'LIM'),
        (3, 'Buenos Aires', 'Argentina', 'EZE'),
        (4, 'Santiago', 'Chile', 'SCL'),
        (5, 'Quito', 'Ecuador', 'UIO'),
        (6, 'Caracas', 'Venezuela', 'CCS'),
        (7, 'Montevideo', 'Uruguay', 'MVD'),
        (8, 'La Paz', 'Bolivia', 'LPB'),
        (9, 'Asunción', 'Paraguay', 'ASU'),
        (10, 'Brasilia', 'Brasil', 'BSB')
    ])
    print("destination populated")

    # Insertar datos en aircraft
    cursor.executemany("""
    INSERT INTO aircraft (AircraftID, FuelNeed, Manufacturer, CapacityPersons)
    VALUES (?, ?, ?, ?);
    """, [
        (1, 2400.0, 'Airbus A320', 150),
        (2, 3600.0, 'Airbus A350', 300),
        (3, 3200.0, 'Boeing 777', 396),
        (4, 2500.0, 'Airbus A380', 555),
        (5, 1800.0, 'Boeing 727', 189),
        (6, 2900.0, 'Airbus A330', 277),
        (7, 2200.0, 'Boeing 737', 162),
        (8, 2700.0, 'Bombardier CRJ', 90),
        (9, 2000.0, 'Embraer 190', 98),
        (10, 2400.0, 'Cessna 208', 14)
    ])
    print("aircraft populated")

    # Insertar datos en pilot
    cursor.executemany("""
    INSERT INTO pilot (PilotID, FirstName, LastName, LicenseNumber, Seniority, EmergencyContact)
    VALUES (?, ?, ?, ?, ?, ?);
    """, [
        (1, 'Carolina', 'Perez', 'L0001', 10, 'Juan Perez'),
        (2, 'Daniel', 'Campos', 'L0002', 8, 'Maria Campos'),
        (3, 'Camilo', 'Torres', 'L0003', 12, 'Sofia Torres'),
        (4, 'Daniel', 'Duran', 'L0004', 6, 'Ana Duran'),
        (5, 'Emilia', 'Rodriguez', 'L0005', 15, 'Luis Rodriguez'),
        (6, 'Camila', 'Castro', 'L0006', 9, 'Fernando Castro'),
        (7, 'Juan', 'Torres', 'L0007', 7, 'Martha Torres'),
        (8, 'Rosa', 'Perdomo', 'L0008', 5, 'Carlos Perdomo'),
        (9, 'Laura', 'Lozano', 'L0009', 11, 'Pedro Lozano')
    ])
    print("pilot populated")

    # Insertar datos en flight
    cursor.executemany("""
    INSERT INTO flight (FlightID, DestinationID, AircraftID, PilotID, DepartureTime, ArrivalTime, Status)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    """, [
        (1, 1, 1, 1, '2024-12-01 08:00:00', '2024-12-01 10:30:00', 'On Time'),
        (2, 2, 2, 2, '2024-12-01 11:00:00', '2024-12-01 14:00:00', 'Delayed'),
        (3, 3, 3, 3, '2024-12-02 09:00:00', '2024-12-02 13:30:00', 'On Time'),
        (4, 4, 4, 4, '2024-12-03 15:00:00', '2024-12-03 19:00:00', 'Cancelled'),
        (5, 5, 5, 5, '2024-12-04 07:30:00', '2024-12-04 11:00:00', 'On Time'),
        (6, 6, 6, 6, '2024-12-05 16:00:00', '2024-12-05 20:30:00', 'On Time'),
        (7, 7, 7, 7, '2024-12-06 06:00:00', '2024-12-06 09:30:00', 'Delayed'),
        (8, 8, 8, 8, '2024-12-07 14:00:00', '2024-12-07 17:30:00', 'On Time'),
        (9, 9, 9, 9, '2024-12-08 10:00:00', '2024-12-08 13:00:00', 'On Time'),
        (10, 10, 10, 1, '2024-12-09 12:00:00', '2024-12-09 15:00:00', 'On Time')
    ])
    print("flight populated")

    connection.commit()
    connection.close()
    print("all tables were populated good")

if __name__ == "__main__":
    create_tables()
    populate_tables()
    view_tables_and_content()


