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
