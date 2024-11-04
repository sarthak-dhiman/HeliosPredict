import pandas as pd
import os
from datetime import datetime , timedelta 
#import xlsxwriter

start_year=2023
start_month=10
start_day=12
end_year=2024
end_month=10
end_day=17

DTF=datetime(start_year,start_month,start_day)
def date_changer():
    start_date = datetime(year=start_year, month=start_month, day=start_day)
    target_date = datetime(year=end_year, month=end_month, day=end_day)
    
    if start_date > target_date:
        print("Start date is after the target date. Please provide a valid range.")
        return
    
    current_date = start_date
    while current_date <= target_date:
        print(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)
    
def concatenate_and_filter_xlsx_files(input_folder, output_file):
    combined_data = pd.DataFrame()

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(input_folder, file_name)
            print(f"Processing file: {file_path}")
            
            df = pd.read_excel(file_path)
            df['time'] = pd.to_datetime(df['time'], errors='coerce').dt.time
            
            start_time = datetime.strptime("08:00", "%H:%M").time()
            end_time = datetime.strptime("22:00", "%H:%M").time()
            filtered_df = df[(df['time'] >= start_time) & (df['time'] <= end_time)]
            
            combined_data = pd.concat([combined_data, filtered_df], ignore_index=True)

    combined_data.to_excel(output_file, index=False)
    print(f"Concatenated and filtered data saved to: {output_file}")

input_folder = r'D:\GithubProject\HelioPredict\WeatherData\Daily(raw)'
output_file = r'D:\GithubProject\HelioPredict\WeatherData\combined_filtered_data.xlsx'

concatenate_and_filter_xlsx_files(input_folder, output_file)









