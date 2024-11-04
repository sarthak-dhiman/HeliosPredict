import requests

def get_location_data(address):
    url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Process the data as needed
        return data
    else:
        return None

# Example usage
address = "Chandigarh"
location_data = get_location_data(address)
if location_data:
    print(location_data)
else:
    print("Failed to retrieve location data.")