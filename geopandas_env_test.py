# Test new Conda env, geopandas, built with Conda-Forge channel

import geopandas as gpd
import fiona

# 2. Create pctgeo, GeoDataframe from file with individual precinct boundaries
# data/pct_area_boulder.geojson
pctgeo = gpd.read_file('data/pct_area_boulder.geojson', driver='GEOJSON')

print(pctgeo.info())
print(pctgeo.head())