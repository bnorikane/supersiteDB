# SupersiteDB

Manage all supersite data for Boulder County Dem Caucus 2024

Run supersite_pct_geom.ipynb to update list of 2024 supersites and precincts

- Bruce Norikane, 2023

## Data Sources

- Supersites
  - 2024 active Supersites - Judi's file
    - data/2024_Supersite_list w Chairs & Cochairs.xlsx
      - Current version - worksheet= "Draft 1-20"
      - Status: Draft - not frozen
  - Venues - any location that could host a Supersite
    - data/supersite_venues_all_years.xlsx
      - supersite name, address, org, lat, lon
      - version: 1/20/2024 - complete and includes 2020 and 2024 and some possible alternates
- Precincts
  - data/pct_area_boulder.geojson
    - list of all Boulder County Precincts after 2022 reprecincting
    - pct, precinctname, CD, HD, SD, border_geom

## Output files

- data/supersites_geom_2024.xlsx
- data/supersites_location_geom_2024.geojson
- data/supersites_region_geom.geojson
- data/supersite_areas_DRAFT.xlsx
- data/venues_all_years_fixed.xlsx

## Code

- supersite_pct_geom.ipynb

  - process Judi's supersite list's embedded precinct lists
    - create supersites_geom_2024.xlsx
      - list of 2024 active supersites
      - supersite name, address, location_geom, border_geom
  - produce precinct to supersite mapping table
  - produce supersite boundary geometry
  - add address, url, and location geometry to

- supersites.py

  - module with supersite processing functions

- index.html
  - Leaflet map showing supersite locations and regions
  - supersite_map.js

## To Do

## Done

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
