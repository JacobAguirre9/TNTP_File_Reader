import os
import re
import shutil
from tqdm import tqdm

def extract_city_name(file_name):
    match = re.match(r"([^_]+(?:-[^_]+)*)_", file_name)
    return match.group(1) if match else None

def create_city_folders(base_path, city_names):
    city_output_dir = os.path.join(base_path, 'City_Specific_Data')
    os.makedirs(city_output_dir, exist_ok=True)

    city_folders = {city: os.path.join(city_output_dir, city) for city in city_names}
    for folder in city_folders.values():
        os.makedirs(folder, exist_ok=True)
    
    return city_folders

def move_files_to_city_folders(base_path, cleaned_folders, city_folders):
    for folder in cleaned_folders:
        folder_path = os.path.join(base_path, folder)
        if os.path.exists(folder_path):
            files = os.listdir(folder_path)
            for file in tqdm(files, desc=f"Processing {folder}", unit="file"):
                city_name = extract_city_name(file)
                if city_name in city_folders:
                    src_file_path = os.path.join(folder_path, file)
                    dst_file_path = os.path.join(city_folders[city_name], file)
                    shutil.move(src_file_path, dst_file_path)

def organize_city_data(base_path):
    # Define the cleaned folders to search in
    cleaned_folders = ['_net_cleaned', '_Nodes_cleaned', '_trips_cleaned', '_node_cleaned', '_flow_cleaned']
    
    # Set to store unique city names
    unique_city_names_cleaned = set()
    
    # Extract city names from cleaned folders
    for folder in cleaned_folders:
        folder_path = os.path.join(base_path, folder)
        if os.path.exists(folder_path):
            files = os.listdir(folder_path)
            for file in files:
                city_name = extract_city_name(file)
                if city_name:
                    unique_city_names_cleaned.add(city_name)
    
    # Create city-specific folders
    city_folders = create_city_folders(base_path, unique_city_names_cleaned)
    
    # Move respective files to city-specific folders
    move_files_to_city_folders(base_path, cleaned_folders, city_folders)
    
    print("Files have been organized into city-specific folders.")

# Example usage:
base_path = '/Users/jacobaguirre/Documents/Github Repositories/TNTP_File_Reader/TransportationNetworks'
organize_city_data(base_path)
