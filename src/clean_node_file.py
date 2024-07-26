import pandas as pd
import os

def clean_node_file(file_path):
    # Extract the city name from the file path
    city_name = os.path.basename(file_path).replace('_node.tntp', '')
    output_csv_path = f'/mnt/data/{city_name}_node_cleaned.csv'
    
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
        if not line.strip():
            continue
        parts = line.split()
        if parts[-1] == ';':
            parts = parts[:-1]
        data.append(parts[:3])  # Consider only the first 3 fields

    # Convert to DataFrame
    columns = ["Node", "X", "Y"]
    df = pd.DataFrame(data, columns=columns)

    # Remove duplicate rows based on all columns
    df = df.drop_duplicates(subset=columns)

    # Save the cleaned data to a CSV file
    df.to_csv(output_csv_path, index=False)
    
    print(f"Cleaned data exported to: {output_csv_path}")

def batch_process_node_files(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter files ending with _node.tntp
    node_files = [f for f in files if f.endswith('_node.tntp')]
    
    # Process each node file
    for node_file in node_files:
        file_path = os.path.join(directory, node_file)
        clean_node_file(file_path)

# Specify the directory to look for _node.tntp files
directory = '/mnt/data/'
batch_process_node_files(directory)
