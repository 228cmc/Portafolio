# Carolina M. Correa

**MSc Computer Science Student | Data Scientist**\
📍 Bath, United Kingdom

---

## About Me

As a passionate MSc Computer Science student and data scientist, I thrive on solving complex problems and creating impactful solutions through programming and data analysis. My academic background in Earth Sciences, coupled with my expertise in software development, equips me with a unique perspective on multidisciplinary challenges.

Throughout my career, I have worked on diverse projects involving AI, data analysis, and software development, leveraging technologies such as Python, Java, SQL, and C. My portfolio demonstrates not only my technical proficiency but also my commitment to continuous learning and growth in the tech industry.

---

## Core Skills

- **Programming Languages:** Python, Java, SQL, C
- **Databases:** SQLite, MySQL
- **Frameworks and Tools:** Flask, Jupyter Notebooks, Git, IntelliJ IDEA
- **Software Development:** Object-Oriented Programming, Data Structures, Algorithms
- **Data Analysis:** Statistical Modeling, Data Visualization
- **Machine Learning:** Regression, Classification, Clustering
- **Cloud Services:** AWS, Docker
- **Agile Practices:** Scrum, CI/CD

---

## Projects

### Python: Flight Management System

A Python-based system to manage flights, pilots, and destinations using an SQLite database.

#### **Technologies:**

- Python, SQLite

#### **Features:**

- Add, update, and view flights, pilots, and destinations.
- Assign pilots to flights and check their schedules.
- Manage and delete data efficiently.

#### **How to Run:**

1. Set up the database:
   ```bash
   python database.py
   ```
2. Run the program:
   ```bash
   python main.py
   ```

#### **Folder Structure:**

```plaintext
Airline_Project/
├── main.py
├── flight.py
├── pilot.py
├── destination.py
├── validation.py
├── database.py
├── flight_management.db
```

---

### Java: Dungeon of Doom

A text-based Java game where players navigate a board to collect gold, avoid a pursuing bot, and escape through an exit.

#### **Technologies:**

- Java

#### **Features:**

- Interactive commands like LOOK, MOVE, PICKUP, and QUIT.
- Object-oriented design principles, including encapsulation and inheritance.
- Validations to ensure proper game setup.

#### **How to Run:**

1. Compile:
   ```bash
   javac Main.java
   ```
2. Run:
   ```bash
   java Main <file_path>
   ```

#### **Example board file:** `exampleBoard.txt`

#### **Folder Structure:**

```plaintext
DungeonDoom/
├── Main.java
├── Board.java
├── BotPlayer.java
├── HumanPlayer.java
├── Player.java
├── Wall.java
├── Gold.java
├── EmptyFloor.java
├── exampleBoard.txt
```

---

### Python: JobScraper

A Python-based project designed to scrape job postings from the MyFuture job portal, save the data in a SQLite database, and provide a web interface using Flask to view and manage the scraped job postings. Additionally, the job data can be exported to a CSV file for further use.

#### **Technologies:**

- Python, SQLite, Flask

#### **Features:**

- Automated Job Scraping: Logs into MyFuture, searches for jobs based on user-defined parameters, and retrieves job details.
- Database Management: Stores the scraped job data in a SQLite database (`db/jobs.db`).
- CSV Export: Exports job data to a CSV file (`jobs_export.csv`) for easy sharing and analysis.
- Web Interface: Provides a Flask-based web interface to view job postings and refresh the database with new job postings.

#### **How to Run:**

1. Create environment, install requirements, and modify `.env` file.
2. Run the scraper:
   ```bash
   python main.py
   ```
3. Start the Flask web server:
   ```bash
   python app.py
   ```
4. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to view the job postings.

#### **Folder Structure:**

```plaintext
JobScraper/
├── db/
│   ├── database.py
│   ├── jobs.db
├── scraper/
│   ├── scraper.py
├── templates/
│   ├── index.html
├── tests/
├── venv/
├── .env
├── .env_example
├── .gitignore
├── app.py
├── config.py
├── jobs_export.csv
├── main.py
├── README.md
├── requirements.txt
```

#### **Authors:**

- [228cmc](https://github.com/228cmc), [cmc228](https://github.com/cmc228)

---

## Contact

- **📧 Email:** [cmc228@bath.ac.uk](mailto:cmc228@bath.ac.uk)
- **🔗 LinkedIn:** [Carolina Masmela Correa](https://www.linkedin.com/in/carolina-masmela-correa)

