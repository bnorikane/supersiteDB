'''
# Supersite processing functions module
- used in supersite_pct_geom.ipynb
'''
import pandas as pd

# cols = ['CONFIRMED', 'APPROVED', 'CONTRACT FINAL', 'Supersite', 'AC Areas',
#        'Region', 'SD', 'HD', '# of Reg Dems', 'Forecast of  Attendees',
#        '# of Pct's', 'Pct #'s', 'PCT #'s', 'PCT #'s.1', 'PCT #'s.2',
#        'PCT #'s.3', 'PCT #'s.4', 'PCT #'s.5', 'PCT #'s.6', 'PCT #'s.7',
#        'PCT #'s.8', 'PCT #'s.9', 'PCT #'s.10', 'PCT #'s.11', 'PCT #'s.12',
#        'PCT #'s.13', 'PCT #'s.14', 'PCT #'s.15', 'PCT #'s.16', 'PCT #'s.17',
#        'PCT #'s.18', 'PCT #'s.19', 'PCT #'s.20', 'PCT #'s.21', 'PCT #'s.22',
#        'PCT #'s.23', 'PCT #'s.24', '# of Chairs', 'Chair 1', 'Chair Name',
#        'Phone', 'Email', 'Chair 2', 'Chair2 Name', 'Phone.1', 'Email.1',
#        'Chair 3', 'Chair3 Name', 'Phone.2', 'Email.2', 'Chair 4',
#        'chair 4 Name', 'Phone.3', 'eMail', 'Chair 1.1', 'Chair 2.1',
#        'Chair 3.1', 'Chair 4.1', 'Unnamed: 58', 'Sort']

def read_supersite_pct (ssfile, sheetname):
    return (
        pd.read_excel(ssfile, sheet_name=sheetname, skiprows=3)
        .rename(columns={
            "Supersite":"supersite", 
            "# of Reg Dems":"dems", 
            "Forecast of  Attendees":"attendee_forecast", 
            "# of Pct's":"total_precincts" 
            })
        .assign(pctlist = pctstr_to_list)
        .assign(attendee_forecast = lambda df_: (df_['attendee_forecast'] + .5).astype(int))
        [['supersite', 'dems', 'attendee_forecast', 'total_precincts', 'pctlist']]
        )
# FUNCTION: Convert column with string of precinct numbers to series with lists of precincts
#   e.g. for each row: '2, 101, 237, 304,,,,,' to [002, 101, 237, 304]

def pctstr_to_list(ss) :

    # transform each string in the list to a list of precinct numbers
    pctlist = ss["Pct #'s"].str.rstrip(',').str.split(',')
    # pctlist = ss["Pct #'s"].str.strip(',').str.split(',')

    # add leading zeros to single-digit precincts

    pctlist = [ [p.zfill(3) for p in pl] for pl in pctlist]

    # remove spaces from pct strings
    pctlist = [ [p.strip(' ') for p in pl] for pl in pctlist]

    
    return pctlist   


# FUNCTION: Add supersite name column to pctgeo
# ISSUE: needs modification to work as external function

# def add_ss_to_pctgeo(ssdf):

#     for ss in ssdf.index:

#         # get pctlist in first supersite
#         pctlist = ssdf['pctlist'][ss]
#         # print(pctlist, '\n')  # list of pcts in supersite

#         # get supersite name
#         ssname = ssdf.loc[ss,'supersite'] 

#         # loop through each pct in pctlist

#         for p in pctlist:
            
#             # print(p, ssname,'\n')

#             # add supersite name to pctgeo
#             pctgeo.loc[p, 'supersite'] = ssname
#             # print(pctgeo.loc[p, :], '\n')  #  dataframe row
#     return

