import pandas as pd

def merge_files_by_date_time(file1_path, file2_path, output_file):
    # Load both Excel files
    df1 = pd.read_excel(file1_path)
    df2 = pd.read_excel(file2_path)

    # Normalize column names by stripping whitespace and making lowercase
    df1.columns = df1.columns.str.strip().str.lower()
    df2.columns = df2.columns.str.strip().str.lower()

    # Ensure both DataFrames have 'date', 'time', and 'power(kw)'
    if not all(col in df1.columns for col in ['date', 'time']):
        raise ValueError("First file is missing 'date' or 'time' columns.")
    
    if not all(col in df2.columns for col in ['date', 'time', 'power(kw)']):
        raise ValueError("Second file is missing 'date', 'time', or 'power(kw)' columns.")

    # Convert the 'date' column in both DataFrames to datetime (just the date part for df1)
    df1['date'] = pd.to_datetime(df1['date']).dt.date  # Keep only the date part
    df2['date'] = pd.to_datetime(df2['date']).dt.date  # Ensure date consistency in both files

    # Check for any invalid dates or times (optional)
    if df1['date'].isnull().any():
        print("Warning: There are NaT values in the first file's 'date' column.")
    if df2['date'].isnull().any():
        print("Warning: There are NaT values in the second file's 'date' column.")

    # Merge data on 'date' and 'time' columns
    merged_df = pd.merge(df1, df2[['date', 'time', 'power(kw)']], on=['date', 'time'], how='left')

    # Save the merged result to the output file
    merged_df.to_excel(output_file, index=False)
    print(f"Merged file saved to: {output_file}")
# Specify file paths
file1_path = r"D:\GithubProject\HelioPredict\WeatherData\combined_filtered_data.xlsx" # Weather-related data
file2_path = r"D:\GithubProject\HelioPredict\SolarData\combined_solar_data.xlsx"  # Power data
output_file = r'D:\GithubProject\HelioPredict\RTP_Data\solar_production.xlsx'

# Run the merge function
merge_files_by_date_time(file1_path, file2_path, output_file)
