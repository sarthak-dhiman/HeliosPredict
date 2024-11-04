import requests
import os
from datetime import datetime, timedelta
import pandas as pd

API_KEY = "dfe4bf3905df43b7999214000243009"
BASE_URL = "http://api.weatherapi.com/v1/history.json"

# Function to get weather data for a specific date and location
def fetch_weather_data(api_key, location, date):
    params = {
        'key': api_key,
        'q': location,  # Location: e.g., city name or coordinates
        'dt': date      # Date in the format YYYY-MM-DD
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()  # Return the JSON data if successful
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response content: {response.text}")
    except Exception as err:
        print(f"Error occurred: {err}")
    return None

# Function to process the data into a DataFrame
def process_weather_data(data):
    hourly_data = data.get('forecast', {}).get('forecastday', [])[0].get('hour', [])
    
    # Create a list to hold the processed data
    processed_data = []
    
    for hour in hourly_data:
        # Extract the condition text from the condition dictionary
        condition_text = hour['condition']['text'] if 'condition' in hour else None
        # Extract date and time
        time_str = hour['time']
        date_str = time_str.split(" ")[0]
        time_only_str = time_str.split(" ")[1]

        # Append processed information including UV index and cloud cover
        processed_data.append({
            'date': date_str,
            'time': time_only_str,
            'uv_index': hour.get('uv', None),
            'cloud_cover': hour.get('cloud', None), 
            'temp_c': hour['temp_c'],
            'humidity': hour['humidity'],
            'wind_kph': hour['wind_kph'],
            'condition': condition_text
        })
    
    # Create DataFrame from the processed data
    df = pd.DataFrame(processed_data)
    return df

# Main function to fetch and save weather data for a date range
def fetch_and_save_weather_data(api_key, location, start_date, end_date, save_folder):
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        print(f"Fetching weather data for: {date_str}")
        
        weather_data = fetch_weather_data(api_key, location, date_str)
        if weather_data:
            df = process_weather_data(weather_data)
            file_name = f"weather_{date_str}.xlsx"
            save_path = os.path.join(save_folder, file_name)
            df.to_excel(save_path, index=False)
            print(f"Weather data saved to: {save_path}")
        else:
            print(f"Failed to fetch weather data for: {date_str}")
        
        current_date += timedelta(days=1)

if __name__ == "__main__":
    # Example usage
    location = "Hoshiarpur"  # Replace with your location
    start_date = datetime.strptime("2024-10-13", "%Y-%m-%d")
    end_date = datetime.strptime("2024-10-17", "%Y-%m-%d")
    save_folder = r"D:\GithubProject\HelioPredict\WeatherData\Daily(raw)"

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    fetch_and_save_weather_data(API_KEY, location, start_date, end_date, save_folder)

