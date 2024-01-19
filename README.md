# SupersiteDB

Manage all supersite data for a single year

- Bruce Norikane, 2023

## Data Sources

- Supersites
  - data/2024_Supersite_list w Chairs & Cochairs.xlsx
  - data/ss_short_2024_alternate.geojson
  - data/ss_short_2024.geojson
- Precincts
  - data/pct_area_boulder.geojson

## Output files

- data/supersites_region_geom.geojson
- data/ss_short_all.geojson
- data/supersite_venues.xlsx

## To Do

- create supersite_venues.xlsx
  - all known supersite venues from all years
  - name, ssid, address, org, lat, lon, geometry, google map link
  - populate data

## History

- Start: 8/15/2023
- Version 0.3
  - reads Judi's spreadsheet
  - writes precinct to supersite geojson file
  - writes supersite region geojson file
- Branch supersite_locations
  - Start: 1/16/2024
  - reads Judi's spreadsheet
  - writes current supersites locations geojson file
