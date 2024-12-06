

# **Flight Management Database**

## **Overview**
This project manages a database for handling flights, pilots, aircraft, and destinations. It uses SQLite3 as the database engine and Python for interacting with it.

---

## **Folder Structure**

```
/flight_management_project
│
├── database.py         # Main script to create and populate the database
├── README.md           # Documentation file
└── flight_management.db # Automatically generated database (after running `database.py`)
```

---

## **Requirements**
- Python 3.x installed.
- Standard library `sqlite3` (pre-installed with Python).

---

## **Setup**

1. Clone the repository or copy the files to your local machine:
   ```bash
   git clone <REPO-URL>
   cd flight_management_project
   ```



---
## **Workflow Explanation**

1. **First:** Run `database.py` to initialize the database and populate it with sample data.
2. **Next:** Use other scripts to manipulate and query the database as needed (if adding future extensions).

## **Usage**

Run `database.py`


please run this just once and if you want to run it again eliminate the file flight_management.pdb and run it again

- If the tables already exist or are populated, the script will detect this and exit gracefully with messages such as:
   ```
   Tables already exist. Exiting setup.
   Tables already populated. Exiting.
   ```

- At the end of the execution, all tables and their contents will be displayed in the console.

---

## module database .py

### 1. **`create_tables()`**
- **Purpose**: 
  Creates the required tables (`Destinations`, `Aircrafts`, `Pilots`, `Flights`) in the database.
- **Details**:
  - If the tables already exist, the function stops execution and displays: `Tables already exist. Exiting setup.`

### 2. **`populate_tables()`**
- **Purpose**: 
  Populates the tables with sample data if they are empty.
- **Details**:
  - Checks if the key table (`Destinations`) contains records before populating.
  - If the tables are already populated, it displays: `Tables already populated. Exiting.`

### 3. **`is_table_empty(cursor, table_name)`**
- **Purpose**:
  Verifies whether a specific table is empty.
- **Usage**:
  - Called within `populate_tables()` to determine whether data insertion is required.

### 4. **`view_tables_and_content()`**
- **Purpose**: 
  Lists all tables in the database and displays their content in the console.
- **Details**:
  - Useful for verifying that the tables and data were created correctly.

---



---

## **Additional Notes**
- If you need to reset the database, delete the `flight_management.db` file manually and re-run `database.py`.

---

## **Contributions**
To extend this project, you could:
- Add new tables (e.g., `Airlines` or `Maintenance`).
- Create an interactive script for dynamic queries.
- Integrate with external APIs for real-world flight or destination data.

