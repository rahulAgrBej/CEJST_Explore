
import requests
import pprint
import pandas as pd

# GET US CENSUS API KEY
f = open('us_census_api_key.txt', 'r')
acs_api_key = f.read().rstrip('\n')
f.close()

# Get a list of all state FIPS
states_fips = list(pd.read_csv('data/census/fips_states_2010.csv', dtype={0:str})['fips'])
print(states_fips)

# General format for ACS data retrieval for all census tracts in a state
ACS_BASE_URL = 'https://api.census.gov/data/2019/acs/acs5?get=NAME,'
ACS_TRACTS = '&for=tract:*&in=state:'
ACS_KEY = '&key=' + acs_api_key

# Specific variables being queried
internet_var = 'B28002_001E'

# build url and send api request
result = None
for fip in states_fips[:2]:
   send_url = ACS_BASE_URL + internet_var + ACS_TRACTS + fip + ACS_KEY
   resp = requests.get(send_url)
   print(resp.status_code)
   if resp.status_code == 200:
      dat = resp.json()
      df = pd.DataFrame(dat)
      result = pd.concat([result, df])
      print(df)
   else:
      print(resp.content)

pp = pprint.PrettyPrinter(indent=3)
#pp.pprint(resp.json())
