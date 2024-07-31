import os
import pandas as pd

def clean_and_export(file_path, output_directory):
    try:
        # Extract the city name from the file path
        city_name = os.path.basename(file_path)
        if city_name.endswith('_net.tntp') or city_name.endswith('_network.tntp'):
            city_name = city_name.replace('_net.tntp', '').replace('_network.tntp', '')
            output_csv_path = os.path.join(output_directory, f'{city_name}_net_cleaned.csv')
            columns = ["init_node", "term_node", "capacity", "length", "free_flow_time", "b", "power", "speed_limit", "toll", "link_type"]
            min_columns = 10
        elif city_name.endswith('_node.tntp') or city_name.endswith('_Nodes.tntp'):
            city_name = city_name.replace('_node.tntp', '').replace('_Nodes.tntp', '')
            output_csv_path = os.path.join(output_directory, f'{city_name}_node_cleaned.csv')
            columns = ["Node", "X", "Y"]
            min_columns = 3
        else:
            raise ValueError("Unsupported file type")

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
            if any(keyword in line for keyword in ["node", "~", "t"]) or not line.strip():
                continue
            parts = line.split()
            if len(parts) >= min_columns:  # Adjusted to handle lines with at least the required fields
                data.append(parts[:min_columns])  # Consider only the required fields

        # Convert to DataFrame
        df = pd.DataFrame(data, columns=columns)

        # Remove duplicate rows based on all columns
        df = df.drop_duplicates()

        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Save the cleaned data to a CSV file
        df.to_csv(output_csv_path, index=False)

        print(f"Cleaned data exported to: {output_csv_path}")
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

def batch_process_files(input_directory, output_directory):
    try:
        # List all files in the input directory
        files = os.listdir(input_directory)

        # Filter files ending with _net.tntp, _network.tntp, _node.tntp, or _Nodes.tntp
        relevant_files = [f for f in files if f.endswith('_net.tntp') or f.endswith('_network.tntp') or f.endswith('_node.tntp') or f.endswith('_Nodes.tntp')]

        # Process each relevant file
        for relevant_file in relevant_files:
            file_path = os.path.join(input_directory, relevant_file)
            clean_and_export(file_path, output_directory)
    except Exception as e:
        print(f"Failed to process batch: {e}")

# Example usage
input_directory = '/mnt/data/'
output_directory = '/mnt/data/cleaned/'
batch_process_files(input_directory, output_directory)
