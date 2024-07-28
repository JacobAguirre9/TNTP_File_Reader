# TNTP_File_Reader

Welcome to the TNTP_File_Reader repository! This repository contains a set of helper functions and subroutines for efficiently and quickly analyzing and cleaning .TNTP file data, which routinely appears in traffic equilibrium and assignment problems.

## Contents

- **Functions**
  - *clean_and_export*: Cleans network files by removing headers and duplicates.
  - *batch_process_node_files*: Processes multiple node files.
  - *batch_process_trips_files*: Cleans and exports trips data.
  - *batch_process_node_conversion_files*: Processes node conversion files.

## Installation

Clone the repository:
```bash
git clone https://github.com/JacobAguirre9/TNTP_File_Reader.git
cd TNTP_File_Reader
```

## Functions

### `clean_flow_file`

This function reads a `.TNTP` flow file, cleans it by removing metadata, unwanted lines, and duplicates, and then exports the cleaned data to a CSV file.

#### How it works

1. Extracts the city name from the file path.
2. Reads the data from the specified `.TNTP` file and skips the metadata lines up to and including `<END OF METADATA>`.
3. Processes the remaining lines and splits each line into parts ensuring it has at least 4 fields.
4. Converts the data into a DataFrame with specified column names and removes duplicate rows.
5. Ensures the output directory exists and exports the cleaned DataFrame to a CSV file.


#### How to use it

1. Ensure your `.TNTP` file is in the input directory.
2. Call the `clean_flow_file` function with the file path and output directory.

Example usage:

``` python
import os
import pandas as pd

input_directory = '/mnt/data/'
output_directory = '/mnt/data/cleaned/'
batch_process_flow_files(input_directory, output_directory)
```
### `clean_and_export`

This function reads a `.TNTP` network file, cleans it by removing headers, unwanted lines, and duplicates, and then exports the cleaned data to a CSV file.

#### How it works

1. Extracts the city name from the file path.
2. Reads the data from the specified `.TNTP` file and skips the header line and unwanted lines.
3. Splits each line into parts ensuring it has at least 10 fields.
4. Converts the data into a DataFrame with specified column names and removes duplicate rows.
5. Ensures the output directory exists and exports the cleaned DataFrame to a CSV file.

#### How to use it

1. Ensure your `.TNTP` file is in the input directory.
2. Call the `clean_and_export` function with the file path and output directory.

# Example usage
``` python
import os
import pandas as pd

input_directory = '/mnt/data/'
output_directory = '/mnt/data/cleaned/'
batch_process_network_files(input_directory, output_directory)
```

### `clean_node_file`

This function reads a `.TNTP` node file, cleans it by removing headers, unwanted lines, and duplicates, and then exports the cleaned data to a CSV file.

#### How it works

1. Extracts the city name from the file path.
2. Reads the data from the specified `.TNTP` file and skips the header line if it contains `NodeID`.
3. Splits each line into parts ensuring it has the required fields.
4. Converts the data into a DataFrame with specified column names and removes duplicate rows.
5. Ensures the output directory exists and exports the cleaned DataFrame to a CSV file.

#### How to use it

1. Ensure your `.TNTP` file is in the input directory.
2. Call the `clean_node_file` function with the file path and output directory.

### `clean_trips_file`

This function reads a `.TNTP` trips file, cleans it by removing unwanted lines and malformed data, and then exports the cleaned data to a CSV file.

#### How it works

1. Reads the data from the specified `.TNTP` file.
2. Processes the lines to extract relevant data, identifying origins and splitting destination-flow pairs.
3. Converts the data into a DataFrame with specified column names and removes any malformed lines.
4. Ensures the output directory exists and exports the cleaned DataFrame to a CSV file.

#### How to use it

1. Ensure your `.TNTP` file is in the input directory.
2. Call the `clean_trips_file` function with the file path and output directory.

``` python
import os
import pandas as pd

# Example usage
input_directory = '/mnt/data/'
output_directory = '/mnt/data/cleaned/'
batch_process_trips_files(input_directory, output_directory)
```

### `clean_node_file`

This function reads a `.TNTP` node file, cleans it by removing headers, unwanted lines, and duplicates, and then exports the cleaned data to a CSV file.

#### How it works

1. Extracts the city name from the file path.
2. Reads the data from the specified `.TNTP` file and skips the header line if it contains `NodeID`.
3. Splits each line into parts ensuring it has the required fields.
4. Converts the data into a DataFrame with specified column names and removes duplicate rows.
5. Ensures the output directory exists and exports the cleaned DataFrame to a CSV file.

#### How to use it

1. Ensure your `.TNTP` file is in the input directory.
2. Call the `clean_node_file` function with the file path and output directory.

Example usage:

```python
import os
import pandas as pd

# Example usage
input_directory = '/mnt/data/'
output_directory = '/mnt/data/cleaned/'
batch_process_node_files(input_directory, output_directory)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request. 

