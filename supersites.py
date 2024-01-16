import pandas as pd

def read_supersite_pct ():
    supersite_input = 'data/2024_Supersite_list w Chairs & Cochairs.xlsx' # 1/13/2024
    return (
        pd.read_excel(supersite_input, sheet_name='Recap SS & Precinct #s', skiprows=3)
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

    # add leading zeros to single-digit precincts
    pctlist = [ [p.zfill(3) for p in pl] for pl in pctlist]
    
    return pctlist   


# FUNCTION: Add supersite name column to pctgeo

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

