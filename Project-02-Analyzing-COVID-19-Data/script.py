# Import required packages
import requests
import json
import pandas as pd

# 1. EXTRACT

# 1.1. Make a get request to api
url = 'https://api.covidtracking.com/v1/us/daily.json'
response = requests.get(url)

# 1.2. Store daily covid data as a JSON file
if response.status_code == 200:
    daily_covid_data = response.json()
    with open('daily_covid_data.json', 'w') as file:
        json.dump(daily_covid_data, file, indent=2, sort_keys=True)
    print("Daily covid data is successfully stored in \"daily_covid_data.json\" file.")
else:
    print('Request failed with status code: ', response.status_code)

# 2. TRANSFORM

# 2.1. Load daily covid data into a pandas DataFrame
df = pd.read_json('daily_covid_data.json')

print(df.shape) # [420 rows x 25 columns]

# 2.2. Keep only records that include data from all 56 states
df = df[df.states == 56]

print(df.shape) # [357 rows x 25 columns]

# 2.3. Remove unnecessary columns
df = df.drop(columns=
    [
        'dateChecked', 'hash', 'hospitalizedCumulative', 'hospitalizedCurrently', 'hospitalizedIncrease', 'inIcuCumulative',
        'inIcuCurrently', 'lastModified', 'onVentilatorCumulative', 'onVentilatorCurrently', 'pending', 'posNeg', 'states',
        'recovered', 'total'
    ])

print(df.shape) # [357 rows x 10 columns]

# 2.4. Reorder columns
df = df[[
        'date', 'hospitalized', 'death', 'deathIncrease', 'negative', 'negativeIncrease',
        'positive', 'positiveIncrease', 'totalTestResults', 'totalTestResultsIncrease'
       ]]

# 2.5. Rename columns
df.rename(columns=
    {
        'date': 'Date',
        'hospitalized': 'Hospitalized',
        'death': 'Death',
        'deathIncrease': 'Death Increase',
        'negative': 'Negative Tests',
        'negativeIncrease': 'Negative Tests Increase',
        'positive': 'Positive Tests',
        'positiveIncrease': 'Positive Tests Increase',
        'totalTestResults': 'Total Test Results',
        'totalTestResultsIncrease': 'Total Test Results Increase',
    }, inplace=True)

# 2.6. Convert date to datetime
df['Date'] = df.Date.astype('str')
df['Date'] = pd.to_datetime(df.Date.str[0:4] + '-' + df.Date.str[4:6] + '-' + df.Date.str[6:8])

# 2.7. Filter rows for year 2021 only
df = df[df['Date'].dt.year == 2021]

print(df.shape) # [66 rows x 10 columns]

# 3. LOAD

# 3.1. Store transformed daily covid data as a CSV file
df.to_csv('transformed_daily_covid_data.csv')

print("Transformed daily covid data is successfully stored in \"transformed_daily_covid_data.csv\" file.")