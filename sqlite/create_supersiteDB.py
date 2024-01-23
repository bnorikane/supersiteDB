# Create supersiteDB - run once to create DB 

import sqlite3

#############      CONNECT to a db       #################
conn = sqlite3.connect("supersite.db")

#############      Create a CURSOR       #################
c = conn.cursor()

#############      EXECUTE SQL QUERY     #################

# CREATE TABLES

precincts_table = '''CREATE TABLE precincts (
            pct TEXT,
            precinctname TEXT,
            geometry TEXT
            ); '''

c.execute(precincts_table)

pct_area_table = '''CREATE TABLE pct_area (
            pct TEXT,
            precinctname TEXT,
            area_short TEXT,
            cd TEXT,
            sd TEXT,
            hd TEXT,
            geometry TEXT
            ); '''

c.execute(pct_area_table)

venues_table = '''CREATE TABLE venues (
            name TEXT,
            venue_code TEXT,
            address TEXT,
            org TEXT,
            website TEXT,
            gmap_name TEXT,
            gmap_url TEXT,
            lat FLOAT,
            lon FLOAT,
            location_geom TEXT
            ); '''

c.execute(venues_table)

pct_ss_table = '''CREATE TABLE pct_ss (
            pct TEXT,
            precinctname TEXT,
            area_short TEXT,
            cd TEXT,
            sd TEXT,
            hd TEXT,
            geometry TEXT,
            ss24_code
            ); '''

c.execute(pct_ss_table)

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