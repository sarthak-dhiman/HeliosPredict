import urllib.request
from datetime import datetime, timedelta
import os

# Set the download directory
download_directory = r'D:\GithubProject\HelioPredict\SolarData\excel(RAW)\Daily'

# Set the date range
start_date = datetime(2022, 2, 10)
end_date = datetime(2024, 6, 14)

# Create the download directory if it doesn't exist
os.makedirs(download_directory, exist_ok=True)

# Function to generate URLs and download Excel files
def download_files(start_date, end_date):
    base_url = "http://theatouch.in/dist/server/api/CodeIgniter/index.php/v2/Excel/GroupDay"
    sign = "tUYWYYBhUiULNU6g3exmAhPEUUdOCItq4Xf5LoZyOiPHgBOs8wfiy0MgyXNVRqOCYjB8n27IbCPzefoDdq2U%2BA258OxoTrEMs84GItw6alunsb%2BpDq%2FUNXCWevIDMkFnTxbhEtLjB%2FWEqXwbe0zKgA%3D%3D"
    member_id = "SarthakDhiman"
    group_id = "12929"
    language = "0"
    
    current_date = start_date
    while current_date <= end_date:
        # Format the date as a string (YYYY-MM-DD)
        date_str = current_date.strftime('%Y-%m-%d')
        
        # Construct the URL with the dynamic date
        file_url = (f"{base_url}?sign={sign}&inDate={date_str}&MemberID={member_id}"
                     f"&GroupID={group_id}&Language={language}")
        
        # Set the file save path (with destination folder)
        save_path = os.path.join(download_directory, f"data_{date_str}.xlsx")
        
        # Download the file
        try:
            print(f"Downloading file for date: {date_str}")
            urllib.request.urlretrieve(file_url, save_path)
            print(f"File successfully downloaded: {save_path}")
        
        except Exception as err:
            print(f"Error occurred for {date_str}: {err}")

        # Move to the next day
        current_date += timedelta(days=1)

if __name__ == "__main__":
    download_files(start_date, end_date)
