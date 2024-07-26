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
    for line in lines:
        if not line.startswith('~') and not line.startswith('t') and line.strip():
            parts = line.split()
            if len(parts) >= 10:  # Adjusted to handle lines with at least 10 fields
                data.append(parts[:10])  # Consider only the first 10 fields

    # Convert to DataFrame
    columns = ["init_node", "term_node", "capacity", "length", "free_flow_time", "b", "power", "speed_limit", "toll", "link_type"]
    df = pd.DataFrame(data, columns=columns)

    # Save the cleaned data to a CSV file
    df.to_csv(output_csv_path, index=False)
    
    print(f"Cleaned data exported to: {output_csv_path}")

# Example usage
city_name = 'berlin-tiergarten'
clean_and_export(city_name)
