# Create supersiteDB - run once to create DB 

import sqlite3

#############      CONNECT to a db       #################
conn = sqlite3.connect("supersite.db")

#############      Create a CURSOR       #################
c = conn.cursor()

#############      EXECUTE SQL QUERY     #################

# CREATE TABLES

precincts_table = '''CREATE TABLE IF NOT EXISTS  precincts (
            pct INTEGER PRIMARY KEY,
            precinctname TEXT,
            cd TEXT,
            sd TEXT,
            hd TEXT,
            area_short TEXT,
            ss24code TEXT, 
            geometry TEXT
            ); '''

c.execute(precincts_table)

venues_table = '''CREATE TABLE IF NOT EXISTS  venues (
            name TEXT,
            venue_code TEXT,
            address TEXT,
            org TEXT,
            website TEXT,
            gmap_name TEXT,
            gmap_url TEXT,
            lat REAL,
            lon REAL,
            location_geom TEXT
            ss24 INTEGER;
            ); '''

c.execute(venues_table)



# # INSERT VALUES INTO TABLE
# people = [
#          ('Billy', 'Bob', 23),
#          ('Sally', 'Field', 76),
#          ('Jerry', 'Garcia', 81) ]

# c.executemany("INSERT INTO test VALUES (?,?,?)", people )

# # SELECT
# c.execute("SELECT * FROM test WHERE first='Billy';")
# print(c.fetchall())

#############      COMMIT changes        ##################
conn.commit()

#############      CLOSE DB CONNECTION   ##################
conn.close()