import requests

# Define the API endpoint and parameters
url = "https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py"
params = {
    "request": "execute",
    "identifier": "SinglePoint",
    "parameters": "ALLSKY_SFC_SW_DWN",
    "userCommunity": "SSE",
    "tempAverage": "DAILY",
    "outputList": "JSON",
    "lat": "31",
    "lon":"75" ,
    "startDate": "20220101",
    "endDate": "20220131"
}

# Send the API request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Process the data as needed
    # ...
else:
    print("Request failed with status code:", response.status_code)