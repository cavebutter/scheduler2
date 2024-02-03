import sqlite3
import csv

# Create a SQLite database and establish a connection
conn = sqlite3.connect('little_league.db')
cursor = conn.cursor()

# Create 'Leagues' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Leagues(
        ID INTEGER PRIMARY KEY,
        League TEXT
    )
''')

# Create 'Fields' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Fields(
        ID INTEGER PRIMARY KEY,
        Location TEXT,
        Field TEXT,
        League_ID INTEGER,
        Lights INTEGER,
        FOREIGN KEY (League_ID) REFERENCES Leagues(ID)
    )
''')

# Create 'Levels' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Levels(
        ID INTEGER PRIMARY KEY,
        Level TEXT
    )
''')

# Create 'Teams' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Teams(
        ID INTEGER PRIMARY KEY,
        Level_ID INTEGER,
        League_ID INTEGER,
        Name TEXT,
        FOREIGN KEY (Level_ID) REFERENCES Levels(ID),
        FOREIGN KEY (League_ID) REFERENCES Leagues(ID)
    )
''')

# Create 'games_per_week_table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS games_per_week(
    level_id INTEGER, 
    gpw INTEGER,
    FOREIGN KEY (level_id) REFERENCES Levels(ID)
    )
''')

# Create field_level table
cursor.execute('''
CREATE TABLE IF NOT EXISTS field_levels (
field_id INTEGER,
level_id INTEGER,
FOREIGN KEY (field_id) REFERENCES Fields(ID),
FOREIGN KEY (level_id) REFERENCeS Levels(ID)
)
''')

# Create day_time table
cursor.execute('''
CREATE TABLE IF NOT EXISTS day_time (
ID INTEGER PRIMARY KEY,
day_text TEXT,
day_num INTEGER,
start_time TIME
)
''')

# Read data from CSV files and insert into the respective tables

# Leagues
with open('data/leagues.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        league_id, league = row
        cursor.execute('INSERT INTO Leagues (ID, League) VALUES (?, ?)', (league_id, league))

# Fields
with open('data/fields.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        field_id, location, field, league_id, lights = row
        cursor.execute('INSERT INTO Fields (ID, Location, Field, League_ID, Lights) VALUES (?, ?, ?, ?, ?)',
                       (field_id, location, field, league_id, lights))

# Levels
with open('data/levels.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        level_id, level = row
        cursor.execute('INSERT INTO Levels (ID, Level) VALUES (?, ?)', (level_id, level))

# Teams
with open('data/teams.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        team_id, level_id, league_id, name = row
        cursor.execute('INSERT INTO Teams (ID, Level_ID, League_ID, Name) VALUES (?, ?, ?, ?)',
                       (team_id, level_id, league_id, name))

with open('data/games_per_week.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        level_id, gpw = row
        cursor.execute('INSERT INTO games_per_week (level_id, gpw) VALUES (?,?)', (level_id, gpw))

with open('data/field_level.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        field_id, level_id = row
        cursor.execute('INSERT INTO field_levels (field_id, level_id) VALUES (?,?)', (field_id, level_id))

with open('data/day_time.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        id, day_text, day_num, start_time = row
        cursor.execute('INSERT INTO day_time (ID, day_text, day_num, start_time)'
                       'VALUES (?,?,?,?)', (id, day_text, day_num, start_time))
# Commit the changes and close the connection
conn.commit()
conn.close()
