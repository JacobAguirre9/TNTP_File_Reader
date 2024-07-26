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


