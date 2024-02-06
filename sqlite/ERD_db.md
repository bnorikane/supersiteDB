# Create database design from requirements

- Written requirements
- ERD
- DB schema

## Written Requirements for 2024 caucus supersites database

- Supersites

  - properties

    - ssid
    - date
    - start_time
    - end_time
    - venueid
    - venue_name
    - venue_contact_name
    - venue_org

  - foreign keys

    - sschair = Volunteers.vanid
    - sstroubleshooter = Volunteers.volid

  - relations

    - Precincts table

      - (1:n, at least 1 precinct in each Supersite)
      - ssid = Precincts.ss24

    - SSRoles table

      - (n:m) joins Supersites by Roles with Volunteers
      - 0 to 4 Co-Chairs
      - 1 to 14 Registrars
      - 0 to 10 Greeters

    - PCTroles table

      - 1 to 20 Precinct Caucus Captains
      - 1 to 20 Precinct Caucus Secretaries

- SSRoles

  - (n:m) joins Supersites by Roles with Volunteers

  - compound key
    - role (cochair, registrar or greeter)
    - supersite = Supersites.ssid
    - volunteer = Volunteers.volid

- PCTRoles

  - compound key
    - role (pct_captain, pct_sec or po)
    - pct = Precincts.pct
    - volunteer = Volunteers.volid

- Venues for Supersites

  - properties:

    - venueid
    - name
    - short name
    - address
    - organization
    - website
    - location geometry
    - auditorium capacity

  - relations
    - venueid = Supersites.ssid (1:1)

- Precincts

  - properties

    - pct
    - precinctname
    - pct_boundary

  - keys
    - area_short
    - 1 to 2 Precinct Organizers
    - 1 to 2 PSPs
    - 1 Caucus Captain
    - 1 Caucus Secretary

- Volunteers

  - properties
    - volid primary key
    - first name
    - last name
    - ngpid
    - stateid
    - vanid
    - email
    - phone
    - voting address
    - voting precinct
    - keys
      - 0 to many roles

- Areas

  - properties

    - area_short name
    - area_long name
    - area_odb name

    - relations

      - 1 or 2 Area Coordinators in Volunteers table
      - at least one precinct in Precincts table
