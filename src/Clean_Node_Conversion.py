import os
import pandas as pd

def clean_node_file(file_path, output_directory):
    try:
        # Extract the city name from the file path
        city_name = os.path.basename(file_path)
        if city_name.endswith('_node.tntp'):
            city_name = city_name.replace('_node.tntp', '')
        elif city_name.endswith('_Nodes.tntp'):
            city_name = city_name.replace('_Nodes.tntp', '')
        
        output_csv_path = os.path.join(output_directory, f'{city_name}_node_cleaned.csv')

        # Read the data file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Check if the first line is a header and skip it if necessary
        if 'NodeID' in lines[0]:
            lines = lines[1:]

        # Convert the remaining lines to a DataFrame
        data = [line.split() for line in lines]
        df = pd.DataFrame(data, columns=["Node", "X", "Y"])

        # Remove duplicate rows based on all columns
        df = df.drop_duplicates(subset=["Node", "X", "Y"])

        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Save the cleaned data to a CSV file
        df.to_csv(output_csv_path, index=False)

        print(f"Cleaned data exported to: {output_csv_path}")
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

def batch_process_node_files(input_directory, output_directory):
    try:
        # List all files in the input directory
        files = os.listdir(input_directory)

        # Filter files ending with _node.tntp or _Nodes.tntp
        node_files = [f for f in files if f.endswith('_node.tntp') or f.endswith('_Nodes.tntp')]

        # Process each node file
        for node_file in node_files:
            file_path = os.path.join(input_directory, node_file)
            clean_node_file(file_path, output_directory)
    except Exception as e:
        print(f"Failed to process batch: {e}")

# Example usage
input_directory = '/mnt/data/'
output_directory = '/mnt/data/cleaned/'
batch_process_node_conversion_files(input_directory, output_directory)
