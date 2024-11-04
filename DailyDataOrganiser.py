import pandas as pd
import os
from datetime import datetime

def concatenate_and_filter_xlsx_files(input_folder, output_file):
    combined_data = pd.DataFrame()

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(input_folder, file_name)
            print(f"Processing file: {file_path}")
            
            # Load the Excel file, skipping the first three rows
            df = pd.read_excel(file_path, header=3)
            print(f"Columns in the file: {df.columns.tolist()}")  # Print column names

            # Normalize column names by stripping whitespace
            df.columns = df.columns.str.strip()
            
            # Ensure the Date column exists
            if 'Date' not in df.columns:
                raise ValueError("The expected 'Date' column is missing.")

            # Display the first few rows for debugging
            print("First few rows of the DataFrame:")
            print(df.head())

            # Convert the Date column to datetime if it's not already
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

            # Check for any conversion issues
            if df['Date'].isnull().any():
                print("There are some invalid dates in the Date column.")

            # Create separate Date and Time columns
            df['date'] = df['Date'].dt.date  # Extract the date part
            df['time'] = df['Date'].dt.time  # Extract the time part
            
            start_time = datetime.strptime("08:00", "%H:%M").time()
            end_time = datetime.strptime("22:00", "%H:%M").time()
            
            # Filter based on the time range
            filtered_df = df[(df['time'] >= start_time) & (df['time'] <= end_time)]
            filtered_df = filtered_df[filtered_df['time'].apply(lambda x: x.minute == 0)]
            
            # Keep only relevant columns: Date and Power (choose one)
            filtered_df = filtered_df[['date', 'time', 'Power(KW)']]  # Ensure this matches your data

            combined_data = pd.concat([combined_data, filtered_df], ignore_index=True)

    combined_data.to_excel(output_file, index=False)
    print(f"Concatenated and filtered data saved to: {output_file}")

input_folder = r'D:\GithubProject\HelioPredict\SolarData\excel(RAW)\Daily'
output_file = r'D:\GithubProject\HelioPredict\SolarData\combined_solar_data.xlsx'

concatenate_and_filter_xlsx_files(input_folder, output_file)
