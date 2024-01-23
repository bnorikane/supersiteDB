# Create supersite db

Move all supersite data into a sqlite database

- Tables
  - precincts
    - pct: 3-digit Boulder County precinct
    - precinctname: 10-digit SoS precinct code
    - geometry: precinct boundary in Shapely/geojson format
  - pct_area
    - pct
    - precinctname
    - area_short: BCDP Field Area code, e.g. LM-06
    - CD
    - SD
    - HD
    - geometry: precinct boundary
  - venues
    - name
    - venue_code
    - address
    - org
    - website
    - gmap_name
    - gmap_url
    - lat
    - lon
    - location_geom
  - pct_ss : list of precincts with supersite
    - pct
    - precinctname
    - area_short
    - CD
    - SD
    - HD
    - geometry
    - ss24_code
