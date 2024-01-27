''' Update table values in supersite.db 
        see create_supersiteDB.py
'''

import pandas as pd
import geopandas as gpd
from shapely import wkt
import sqlite3

# connect to supersite.db
conn = sqlite3.connect("supersite.db")

######      CREATE VENUES TABLE
# use columns and values from the venues spreadsheet
# replace any existing table and load all new values and columns

# create dataframe from supersite_venues_all_years_fixed.xlsx
venues = pd.read_excel('../data/venues_all_years_fixed.xlsx')
# print(venues.info())
# print(venues)

# create venues table from venues dataframe
venues.to_sql('venues', conn, if_exists='replace')

#######     CREATE PRECINCTS TABLE
# use columns and values from precincts spreadsheet
# replace any existing table and load all new values and columns

# create dataframe from pct_area_boulder.xlsX

pct_worksheet = 'pct_area'
pct_spreadsheet = '../data/pct_area_boulder.xlsx'
precincts = pd.read_excel(pct_spreadsheet, sheet_name=pct_worksheet)


print(precincts.info())
# print(precincts)
precincts.to_sql('precincts', conn, if_exists='replace')

# create precincts table from geojson file
# use columns and values from the precincts geojson file
# replace any existing table and load all new values and columns

# create GeoDataFrame from geojson file
# precincts = gpd.read_file('../data/pct_area_boulder.geojson', driver='GeoJSON')

# convert geometry column to text
# gridDF['str_geom'] = gridDF.geometry.apply(lambda x: wkt.dumps(x))
# precincts['geometry'] = precincts['geometry'].apply(lambda x: wkt.dumps(x))





#############      COMMIT changes        ##################
conn.commit()

#############      CLOSE DB CONNECTION   ##################
conn.close()
    
