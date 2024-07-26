import os
import pandas as pd

def clean_node_conversion_file(file_path, output_directory):
    try:
        # Read the data file and clean it
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Skip the header
        data = []
        for line in lines[1:]:
            line = line.strip()
            if line:
                parts = line.split()
                if len(parts) == 2:
                    new_node, original_node = parts
                    try:
                        new_node = int(new_node)
                        original_node = int(original_node)
                        data.append([new_node, original_node])
                    except ValueError:
                        print(f"Skipping malformed line: {line}")
        
        # Convert to DataFrame
        df = pd.DataFrame(data, columns=["New node number", "Original node number"])
        
        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        # Save the cleaned data to a CSV file
        output_csv_path = os.path.join(output_directory, os.path.basename(file_path).replace('.txt', '_cleaned.csv'))
        df.to_csv(output_csv_path, index=False)
        
        print(f"Cleaned data exported to: {output_csv_path}")
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

def batch_process_node_conversion_files(input_directory, output_directory):
    try:
        # List all files in the input directory
        files = os.listdir(input_directory)
        
        # Filter files ending with _Node-Conversion.txt
        conversion_files = [f for f in files if f.endswith('_Node-Conversion.txt')]
        
        # Process each node conversion file
        for conversion_file in conversion_files:
            file_path = os.path.join(input_directory, conversion_file)
            clean_node_conversion_file(file_path, output_directory)
    except Exception as e:
        print(f"Failed to process batch: {e}")

# Example usage
input_directory = '/mnt/data/'
output_directory = '/mnt/data/cleaned/'
batch_process_node_conversion_files(input_directory, output_directory)
