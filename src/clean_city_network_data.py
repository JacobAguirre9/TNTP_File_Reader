import os
import pandas as pd

def clean_and_export(file_path, output_directory):
    try:
        # Extract the city name from the file path
        city_name = os.path.basename(file_path)
        if city_name.endswith('_net.tntp'):
            city_name = city_name.replace('_net.tntp', '')
        
        output_csv_path = os.path.join(output_directory, f'{city_name}_net_cleaned.csv')

        # Read the data file and clean it
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Process the lines to extract relevant data
        data = []
        header_skipped = False
        for line in lines:
            if not header_skipped:
                header_skipped = True
                continue
            if "node" in line or line.startswith('~') or line.startswith('t') or not line.strip():
                continue
            parts = line.split()
            if len(parts) >= 10:  # Adjusted to handle lines with at least 10 fields
                data.append(parts[:10])  # Consider only the first 10 fields

        # Convert to DataFrame
        columns = ["init_node", "term_node", "capacity", "length", "free_flow_time", "b", "power", "speed_limit", "toll", "link_type"]
        df = pd.DataFrame(data, columns=columns)

        # Remove duplicate rows based on all columns
        df = df.drop_duplicates(subset=columns)

        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Save the cleaned data to a CSV file
        df.to_csv(output_csv_path, index=False)

        print(f"Cleaned data exported to: {output_csv_path}")
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

def batch_process_network_files(input_directory, output_directory):
    try:
        # List all files in the input directory
        files = os.listdir(input_directory)

        # Filter files ending with _net.tntp
        network_files = [f for f in files if f.endswith('_net.tntp')]

        # Process each network file
        for network_file in network_files:
            file_path = os.path.join(input_directory, network_file)
            clean_and_export(file_path, output_directory)
    except Exception as e:
        print(f"Failed to process batch: {e}")

# Example usage
input_directory = '/mnt/data/'
output_directory = '/mnt/data/cleaned/'
batch_process_network_files(input_directory, output_directory)
