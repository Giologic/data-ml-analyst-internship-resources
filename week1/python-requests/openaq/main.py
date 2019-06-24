import requests
import os
import json
import pandas as pd

if __name__ == "__main__":
  url = 'https://api.openaq.org/v1'   
  measurements = 'latest'

  

  full_url = os.path.join(url, measurements)
  params = '?city=Manila' 
  full_url = full_url + params
  
  print(full_url)
  response = requests.get(
    full_url,
    data = {},
    headers = {},
  )

  parsed_json = response.json().get('results')[0].get('measurements')[0]
  print(parsed_json)
  df = pd.DataFrame(parsed_json)
  print(df.head())
