here’s the updated readme with the additional instructions about `database.py`:

---

# flight management system

this is a simple system built with python and sqlite to manage flights, pilots, and destinations. it lets you perform basic actions like adding, viewing, and updating information in an easy way.

## features

- **add flights**: create a new flight entry.
- **view flights**: search for flights based on things like origin, destination, status, or departure time.
- **update flights**: change flight details like status or departure time.
- **add pilots**: add new pilots to the system.
- **assign pilots**: link a pilot to a specific flight.
- **view pilot schedule**: check all flights assigned to a specific pilot.
- **delete pilots**: remove pilot information and clear their assigned flights.
- **manage destinations**: update or view details about destinations.

## how to set up the database

before you can use the system, you need to set up the database.

1. **locate the `database.py` file**:
   - this script creates the sqlite database and the necessary tables like `flight`, `pilot`, `destination`, and `aircraft`.

2. **run the script**:
   - open a terminal or command prompt.
   - navigate to the folder where the project files are saved.
   - run the script with the command:
     ```bash
     python database.py
     ```

3. **verify the database is created**:
   - check for the file `flight_management.db` in the project folder.
   - ensure it contains the required tables created by the script.

4. **run the main program**:
   - once the database is set up, you don’t need to run `database.py` again unless you want to reset the database.

## how to run

1. make sure you have python installed on your computer.
2. download or clone the project files.
3. set up the database (see instructions above).
4. open a terminal and run:
   ```bash
   python main.py
   ```

## how to use

1. start the program and follow the menu on your screen.
2. choose the action you want by typing the corresponding number.
3. provide the requested details, like flight info or pilot id.
4. when you're done, choose option 9 to exit.

## project structure

- `main.py`: the main file that runs the system.
- `flight.py`: handles anything related to flights.
- `pilot.py`: takes care of pilots and their assignments.
- `destination.py`: manages destination data.
- `validation.py`: checks user inputs, like numbers and text.
- `database.py`: sets up the sqlite database and tables.
- `flight_management.db`: the sqlite database where data is stored.



---
