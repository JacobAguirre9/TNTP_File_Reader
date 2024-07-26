using HTTP
using Gumbo
using Cascadia
using Downloads

# Function to download file
function download_file(url, folder)
    local_filename = joinpath(folder, split(url, "/")[end])
    Downloads.download(url, local_filename)
    return local_filename
end

# Function to create directories dynamically based on suffix
function create_directories(base_path, suffixes)
    for suffix in suffixes
        dir_path = joinpath(base_path, replace(suffix, ".tntp" => ""))
        if !isdir(dir_path)
            mkpath(dir_path)
        end
    end
end

# Function to extract suffix from filename
function extract_suffix(filename)
    return filename[findlast('_', filename):end]
end

# Base URL of the GitHub repository
base_url = "https://github.com/bstabler/TransportationNetworks/tree/master"

# Directory to save the downloaded files
base_path = "./TransportationNetworks"

# Get the HTML content of the base URL
response = HTTP.get(base_url)
soup = parsehtml(String(response.body))

# Find all links to city folders in the repository
city_links = eachmatch(Selector("a[href*='/tree/master/']"), soup.root)
city_folders = [link.attributes["href"] for link in city_links if occursin("/tree/master/", link.attributes["href"])]

# Dictionary to hold suffixes
suffixes = Set{String}()

# Loop through city folders and prepare to download the relevant files
for city_folder in city_folders
    city_url = "https://github.com" * city_folder
    city_response = HTTP.get(city_url)
    city_soup = parsehtml(String(city_response.body))
    file_links = eachmatch(Selector("a[href*='.tntp']"), city_soup.root)
    
    for link in file_links
        file_url = link.attributes["href"]
        if endswith(file_url, ".tntp")
            # Extract the suffix
            suffix = extract_suffix(file_url)
            push!(suffixes, suffix)
        end
    end
end

# Create directories for each suffix
create_directories(base_path, suffixes)

# Loop through city folders and download the relevant files
for city_folder in city_folders
    city_url = "https://github.com" * city_folder
    city_response = HTTP.get(city_url)
    city_soup = parsehtml(String(city_response.body))
    file_links = eachmatch(Selector("a[href*='.tntp']"), city_soup.root)
    
    total_files = length(file_links)
    for (i, link) in enumerate(file_links)
        file_url = link.attributes["href"]
        if endswith(file_url, ".tntp")
            # Extract the suffix and determine the folder
            suffix = extract_suffix(file_url)
            folder = joinpath(base_path, replace(suffix, ".tntp" => ""))
            
            # Construct the full URL to the raw file
            raw_file_url = replace(file_url, "blob" => "raw")
            
            # Download the file
            download_file("https://github.com$raw_file_url", folder)
            println("Downloaded $file_url to $folder ($i/$total_files)")
        end
    end
end

println("All files have been downloaded and organized.")
