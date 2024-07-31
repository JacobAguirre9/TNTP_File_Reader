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
        elif city_name.endswith('_nodes.tntp'):
            city_name = city_name.replace('_nodes.tntp', '')

        output_csv_path = os.path.join(output_directory, f'{city_name}_node_cleaned.csv')

        # Read the data file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Detect and remove the header line, if present
        header = None
        if 'Node' in lines[0] or 'node' in lines[0]:
            header = lines[0].strip().strip(';').split()
            lines = lines[1:]

        # Handle different delimiters and trailing semicolons
        data = []
        for line in lines:
            line = line.strip().strip(';')  # Remove trailing semicolons and whitespace
            if line:
                data.append(line.split())

        # Determine the number of columns dynamically
        if header:
            columns = header
        else:
            num_columns = len(data[0])
            if num_columns == 3:
                columns = ["Node", "X", "Y"]
            else:
                raise ValueError(f"Unexpected number of columns: {num_columns}")

        # Create a DataFrame with the appropriate columns
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

def batch_process_node_files(input_directory, output_directory):
    try:
        # List all files in the input directory
        files = os.listdir(input_directory)

        # Filter files ending with _node.tntp or _Nodes.tntp or _nodes.tntp
        node_files = [file for file in files if file.endswith('_node.tntp') or file.endswith('_Nodes.tntp') or file.endswith('_nodes.tntp')]

        # Process each node file
        for node_file in node_files:
            file_path = os.path.join(input_directory, node_file)
            clean_node_file(file_path, output_directory)
    except Exception as e:
        print(f"Failed to process batch: {e}")

# Example usage
input_directory = '/Users/jacobaguirre/Documents/Github Repositories/TNTP_File_Reader/TransportationNetworks/_01'
output_directory = '/Users/jacobaguirre/Documents/Github Repositories/TNTP_File_Reader/TransportationNetworks/_node_cleaned'
batch_process_node_files(input_directory, output_directory)
