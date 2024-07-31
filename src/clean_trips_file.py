import os
import pandas as pd

def clean_trips_file(file_path, output_directory):
    try:
        # Read the data file and clean it
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        data = []
        origin = None
        for line in lines:
            line = line.strip()
            if line.startswith('Origin'):
                origin = int(line.split()[1])
            elif ':' in line:
                parts = line.split(';')
                for part in parts:
                    if ':' in part:
                        destination, flow = part.split(':')
                        try:
                            destination = int(destination.strip())
                            flow = float(flow.strip())
                            data.append([origin, destination, flow])
                        except ValueError:
                            print(f"Skipping malformed line: {line}")
                            continue

        # Convert to DataFrame
        df = pd.DataFrame(data, columns=["Origin", "Destination", "Flow"])
        
        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        # Save the cleaned data to a CSV file
        output_csv_path = os.path.join(output_directory, os.path.basename(file_path).replace('.tntp', '_cleaned.csv'))
        df.to_csv(output_csv_path, index=False)
        
        print(f"Cleaned data exported to: {output_csv_path}")
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

def batch_process_trips_files(input_directory, output_directory):
    try:
        # List all files in the input directory
        files = os.listdir(input_directory)
        
        # Filter files ending with _trips.tntp
        trips_files = [f for f in files if f.endswith('_trips.tntp')]
        
        # Process each trips file
        for trips_file in trips_files:
            file_path = os.path.join(input_directory, trips_file)
            clean_trips_file(file_path, output_directory)
    except Exception as e:
        print(f"Failed to process batch: {e}")

# Example usage
input_directory = '/mnt/data/'
output_directory = '/mnt/data/cleaned/'
batch_process_trips_files(input_directory, output_directory)