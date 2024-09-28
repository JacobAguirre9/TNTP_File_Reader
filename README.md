# TNTP_File_Reader

This repository provides a set of scripts for efficiently analyzing, cleaning, and visualizing `.TNTP` file data, commonly used in traffic equilibrium and assignment problems. The scripts are enhanced with logging, command-line interfaces, data validation, and comprehensive visualizations to facilitate robust data processing and insightful analysis.

**Authors:** Jacob M. Aguirre and Anton J. Kleywegt

Should you have any comments or recommendations, please contact us at `first author lastname @ gatech dot edu`.


## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Scripts](#scripts)
  - [1. `clean_city_network_data.py`](#1-clean_city_network_datapy)
  - [2. `clean_flow_files.py`](#2-clean_flow_filespy)
  - [3. `Clean_Node_Conversion.py`](#3-clean_node_conversionpy)
  - [4. `clean_trips_file.py`](#4-clean_trips_filepy)
  - [5. `organize_city_data.py`](#5-organize_city_datapy)
  - [6. `summary_statistics.py`](#6-summary_statisticspy)
- [Usage](#usage)
- [License](#license)

## Features

- **Logging:** Comprehensive logging using Python’s `logging` module for better monitoring and debugging.
- **Command-Line Interface (CLI):** Flexible script execution with `argparse` for specifying input/output directories and logging levels.
- **Data Validation:** Ensures data integrity by enforcing data types and validating input data.
- **Visualization:** Generates insightful graphs and plots using `matplotlib`, `seaborn`, and `networkx` to enhance data understanding.
- **Modularity:** Structured with clear, modular functions for maintainability and scalability.
- **Error Handling:** Robust exception handling with detailed error messages and stack traces.
- **Progress Tracking:** Utilizes `tqdm` for progress bars during batch processing tasks.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/JacobAguirre9/TNTP_File_Reader.git
    cd TNTP_File_Reader
    ```

2. **Create a Virtual Environment (Optional but Recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    *`requirements.txt` content:*

    ```plaintext
    pandas
    matplotlib
    seaborn
    networkx
    tqdm
    ```
   To get the latest version, use
   ```bash
   pip install --upgrade -r requirements.txt
   ```

## Scripts

### 1. `clean_city_network_data.py`

Cleans network and node `.TNTP` data files by removing headers, unwanted lines, duplicates, and exports the cleaned data as CSV files. Additionally, it generates network graphs and node location plots for enhanced visualization.

#### Key Features

- **Network Data Cleaning:** Processes files ending with `_net.tntp` or `_network.tntp`.
- **Node Data Cleaning:** Processes files ending with `_node.tntp` or `_Nodes.tntp`.
- **Visualization:** Generates network graphs using `networkx` and node location scatter plots.

#### Example Usage

```bash
python3 clean_city_network_data.py --input_dir "/path/to/input" --output_dir "/path/to/output" --log_level INFO
```

### 2. `clean_flow_files.py`

Cleans flow `.TNTP` files by removing metadata, unwanted lines, duplicates, and exports the cleaned data as CSV files. It also generates flow distribution histograms and scatter plots to visualize flow patterns.

#### Key Features

- **Flow Data Cleaning:** Processes files ending with `_flow.tntp`.
- **Visualization:** Generates volume and cost distribution histograms, and volume vs. cost scatter plots.

#### Example Usage

```bash
python3 clean_flow_files.py --input_dir "/path/to/input" --output_dir "/path/to/output" --log_level INFO
```

### 3. `Clean_Node_Conversion.py`

Cleans node conversion `.TNTP` files by removing headers, unwanted lines, and duplicates, then exports the cleaned data as CSV files.

#### Key Features

- **Node Conversion Data Cleaning:** Processes files ending with `_node.tntp`, `_Nodes.tntp`, or `_nodes.tntp`.
- **Data Validation:** Ensures correct data types for node identifiers and coordinates.

#### Example Usage

```bash
python3 Clean_Node_Conversion.py --input_dir "/path/to/input" --output_dir "/path/to/output" --log_level INFO
```

### 4. `clean_trips_file.py`

Cleans trip `.TNTP` files by removing headers, unwanted lines, duplicates, and exports the cleaned data as CSV files. It also generates visualizations such as flow distribution histograms and trips per origin bar charts.

#### Key Features

- **Trip Data Cleaning:** Processes files ending with `_trips.tntp`.
- **Visualization:** Generates flow distribution histograms, trips per origin bar charts, and flow vs. origin scatter plots.

#### Example Usage

```bash
python3 clean_trips_file.py --input_dir "/path/to/input" --output_dir "/path/to/output" --log_level INFO
```

### 5. `organize_city_data.py`

Organizes cleaned data files into city-specific folders for better management and analysis. It scans through various cleaned data directories and moves files into corresponding city folders.

#### Key Features

- **Organization:** Moves cleaned network, node, flow, and trip CSV files into dedicated city directories.
- **Progress Tracking:** Displays progress bars using `tqdm` during the file-moving process.

#### Example Usage

```bash
python3 organize_city_data.py --base_path "/path/to/TransportationNetworks" --log_level INFO
```

### 6. `summary_statistics.py`

Computes meaningful statistics and generates visualizations from the organized city data. It processes network, node, flow, and trip data to provide comprehensive insights into each city's transportation network.

#### Key Features

- **Statistics Computation:** Calculates metrics such as the number of nodes and links, average capacity and length, total and average flow, and trip statistics.
- **Visualization:** Generates bar charts, scatter plots, and histograms to visualize the computed statistics.
- **Summary Export:** Saves a summary CSV file containing all computed statistics.

#### Example Usage

```bash
python3 summary_statistics.py --input_dir "/path/to/City_Specific_Data" --output_dir "/path/to/Statistics_Output" --log_level INFO
```

## Usage

1. **Prepare Your Data:**

    - Ensure your `.TNTP` files are placed in the designated input directories.
    - Use the cleaning scripts (`clean_city_network_data.py`, `clean_flow_files.py`, etc.) to process and clean your data.

2. **Organize Cleaned Data:**

    - Run `organize_city_data.py` to structure your cleaned data into city-specific folders.

3. **Generate Summary Statistics:**

    - Execute `summary_statistics.py` to compute statistics and generate visualizations from the organized data.

4. **Review Outputs:**

    - Check the specified output directories for cleaned CSV files and generated visualizations (graphs and plots).

5. **Adjust Logging Levels (Optional):**

    - Use the `--log_level` argument to set the desired logging verbosity (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).

## License

This project is licensed under the [MIT License](LICENSE).

```
