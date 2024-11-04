key="0956da4251ce47acbf7192019241009"
import requests
# home coords 31.525560257522006, 75.94976086598646

API_KEY = "0956da4251ce47acbf7192019241009"
location = "Hoshiarpur"  # You can also use coordinates like "51.5074,0.1278"

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}"

response = requests.get(url)
weather_data = response.json()

print("Location:", weather_data['location']['name'])
print("Temperature (C):", weather_data['current']['temp_c'])
print("Weather Condition:", weather_data['current']['condition']['text'])
print("Wind Speed (kph):", weather_data['current']['wind_kph'])
print("Humidity:", weather_data['current']['humidity'])

# Coordinates for the location
lat = "1.36515"
lon = "80.22"

def get_solar_radiation(lat, lon, start_date, end_date):
    # NASA POWER API endpoint
    url = f"https://power.larc.nasa.gov/api/temporal/daily/point?start={start_date}&end={end_date}&latitude={lat}&longitude={lon}&parameters=ALLSKY_SFC_SW_DWN&format=json"
    
    # Make the request to NASA POWER API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Extract solar radiation data (W/m²)
        solar_radiation = data['properties']['parameter']['ALLSKY_SFC_SW_DWN']
        return solar_radiation
    else:
        print(f"Error: {response.status_code}")
        return None

# Exam
