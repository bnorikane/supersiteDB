# Create supersiteDB - run once to create DB 

import sqlite3
import pandas as pd

#############      CONNECT to a db       #################
conn = sqlite3.connect("supersite.db")

#############      Create a CURSOR       #################
c = conn.cursor()

#############      EXECUTE SQL QUERY     #################

# CREATE TABLES

precincts_table = '''CREATE TABLE IF NOT EXISTS  precincts (
            pct INTEGER PRIMARY KEY,
            precinctname TEXT NOT NULL,
            cd TEXT,
            sd TEXT,
            hd TEXT,
            area_short TEXT,
            ss24_id INTEGER, 
            geometry TEXT
            ); '''

c.execute(precincts_table)

venues_table = '''CREATE TABLE IF NOT EXISTS  venues (
            venue_id INTEGER PRIMARY KEY,
            venue TEXT NOT NULL,
            venue_code,
            address TEXT,
            org TEXT,
            website TEXT,
            gmap_url TEXT,
            gmap_name TEXT,
            lat REAL,
            lon REAL,
            location_geom TEXT
            ); '''

c.execute(venues_table)


# Insert values into tables
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