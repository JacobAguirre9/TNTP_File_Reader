import os
import pandas as pd

def clean_flow_file(file_path, output_directory):
    try:
        # Extract the city name from the file path
        city_name = os.path.basename(file_path).replace('_flow.tntp', '')
        output_csv_path = os.path.join(output_directory, f'{city_name}_flow_cleaned.csv')

        # Read the data file and clean it
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Find the start of the actual data
        start_index = 0
        for i, line in enumerate(lines):
            if '<END OF METADATA>' in line:
                start_index = i + 1
                break

        # Read the data from the lines after the metadata
        data = []
        for line in lines[start_index:]:
            if not line.strip():
                continue
            if 'Tail,Head,Volume,Cost' in line:
                line = 'From,To,Volume,Cost'  # Replace the header
                continue
            parts = line.split()
            if parts[-1] == ';':
                parts = parts[:-1]
            data.append(parts[:4])  # Consider only the first 4 fields

        # Convert to DataFrame
        columns = ["From", "To", "Volume", "Cost"]
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

def batch_process_flow_files(input_directory, output_directory):
    try:
        # List all files in the input directory
        files = os.listdir(input_directory)

        # Filter files ending with _flow.tntp
        flow_files = [f for f in files if f.endswith('_flow.tntp')]

        # Process each flow file
        for flow_file in flow_files:
            file_path = os.path.join(input_directory, flow_file)
            clean_flow_file(file_path, output_directory)
    except Exception as e:
        print(f"Failed to process batch: {e}")

# Example usage
input_directory = 'TransportationNetworks/_flow'
output_directory = 'TransportationNetworks/_flow_cleaned'
batch_process_flow_files(input_directory, output_directory)
