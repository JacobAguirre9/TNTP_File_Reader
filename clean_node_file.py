import pandas as pd

def clean_node_file(city_name):
    # Construct file paths
    input_file_path = f'/mnt/data/{city_name}_node.tntp'
    output_csv_path = f'/mnt/data/{city_name}_node_cleaned.csv'
    
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
        if not line.strip():
            continue
        parts = line.split()
        if parts[-1] == ';':
            parts = parts[:-1]
        data.append(parts[:3])  # Consider only the first 3 fields

    # Convert to DataFrame
    columns = ["Node", "X", "Y"]
    df = pd.DataFrame(data, columns=columns)

    # Save the cleaned data to a CSV file
    df.to_csv(output_csv_path, index=False)
    
    print(f"Cleaned data exported to: {output_csv_path}")

# Example usage
city_name = 'berlin-center'
clean_node_file(city_name)

# Display the first 5 rows of the cleaned data
df = pd.read_csv(f'/mnt/data/{city_name}_node_cleaned.csv')
df.head()
