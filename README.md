# TNTP_File_Reader

This repository provides a set of helper functions and subroutines for efficiently and quickly analyzing and cleaning .TNTP file data, which routinely appears in traffic equilibrium and assignment problems.

## Functions

### `clean_and_export`

This function reads a `.TNTP` network file, cleans it by removing headers, unwanted lines, and duplicates, and then exports the cleaned data to a CSV file.

#### How it works

1. Reads the data from the specified `.TNTP` file.
2. Skips the header line and any unwanted lines (lines starting with '~', 't', or empty lines).
3. Splits each line into parts and ensures it has at least 10 fields.
4. Converts the data into a DataFrame with specified column names.
5. Removes any duplicate rows based on all columns.
6. Exports the cleaned DataFrame to a CSV file.

#### How to use it

1. Ensure your `.TNTP` file is in the `/mnt/data/` directory.
2. Call the `clean_and_export` function with the appropriate city name (the file should follow the pattern `cityname_net.tntp`).

Example usage:

```python
import pandas as pd

def clean_and_export(city_name):
    # Construct file paths
    input_file_path = f'/mnt/data/{city_name}_net.tntp'
    output_csv_path = f'/mnt/data/{city_name}_net_cleaned.csv'
    
    # Read the data file and clean it
    with open(input_file_path, 'r') as file:
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

    # Save the cleaned data to a CSV file
    df.to_csv(output_csv_path, index=False)
    
    print(f"Cleaned data exported to: {output_csv_path}")

# Example usage
city_name = 'friedrichshain-center'
clean_and_export(city_name)

# Display the first 5 rows of the cleaned data
df = pd.read_csv(f'/mnt/data/{city_name}_net_cleaned.csv')
df.head()
```

### `batch_process_node_files`

This function scans a specified directory for files ending with `_node.tntp`, cleans them by removing headers, unwanted lines, and duplicates, and then exports the cleaned data to CSV files.

#### How it works

1. Lists all files in the specified directory.
2. Filters the files to include only those ending with `_node.tntp`.
3. For each filtered file:
   - Reads the data from the file.
   - Skips the header row and any unwanted lines.
   - Splits each line into parts and ensures it has at least 3 fields.
   - Converts the data into a DataFrame with specified column names.
   - Removes any duplicate rows based on all columns.
   - Exports the cleaned DataFrame to a CSV file.

#### How to use it

1. Ensure your `.TNTP` files are in the `/mnt/data/` directory.
2. Call the `batch_process_node_files` function with the directory path.

Example usage:

```python
import pandas as pd
import os

def clean_node_file(file_path):
    city_name = os.path.basename(file_path).replace('_node.tntp', '')
    output_csv_path = f'/mnt/data/{city_name}_node_cleaned.csv'
    with open(file_path, 'r') as file:
        lines = file.readlines()
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
        data.append(parts[:3])
    columns = ["Node", "X", "Y"]
    df = pd.DataFrame(data, columns=columns)
    df = df.drop_duplicates(subset=columns)
    df.to_csv(output_csv_path, index=False)
    print(f"Cleaned data exported to: {output_csv_path}")

def batch_process_node_files(directory):
    files = os.listdir(directory)
    node_files = [f for f in files if f.endswith('_node.tntp')]
    for node_file in node_files:
        file_path = os.path.join(directory, node_file)
        clean_node_file(file_path)

# Example usage
batch_process_node_files('/mnt/data/')
```
### `batch_process_trips_files`

This function scans a specified directory for files ending with `_trips.tntp`, cleans them by removing headers, unwanted lines, and duplicates, and then exports the cleaned data to a user-specified directory.

#### How it works

1. Lists all files in the specified input directory.
2. Filters the files to include only those ending with `_trips.tntp`.
3. For each filtered file:
   - Reads the data from the file.
   - Skips the metadata lines.
   - Parses origin and destination data.
   - Converts the data into a DataFrame with specified column names.
   - Removes any malformed lines.
   - Exports the cleaned DataFrame to a CSV file in the user-specified output directory.

#### How to use it

1. Ensure your `.TNTP` files are in the input directory.
2. Call the `batch_process_trips_files` function with the input and output directory paths.

Example usage:

```python
import os
import pandas as pd

def clean_trips_file(file_path, output_directory):
    try:
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
        
        df = pd.DataFrame(data, columns=["Origin", "Destination", "Flow"])
        
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        output_csv_path = os.path.join(output_directory, os.path.basename(file_path).replace('.tntp', '_cleaned.csv'))
        df.to_csv(output_csv_path, index=False)
        
        print(f"Cleaned data exported to: {output_csv_path}")
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

def batch_process_trips_files(input_directory, output_directory):
    try:
        files = os.listdir(input_directory)
        trips_files = [f for f in files if f.endswith('_trips.tntp')]
        for trips_file in trips_files:
            file_path = os.path.join(input_directory, trips_file)
            clean_trips_file(file_path, output_directory)
    except Exception as e:
        print(f"Failed to process batch: {e}")

# Example usage
input_directory = '/mnt/data/'
output_directory = '/mnt/data/cleaned/'
batch_process_trips_files(input_directory, output_directory)


