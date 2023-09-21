"""This file will be used to store the data collected. It will be stored in JSON format,
and will be processed from there"""

import logging
import os
import json
from datetime import datetime
from parse_data import parse
from fetcher import fetcher

# Create a data directory if it doesn't exist
if not os.path.exists("Web-Scraper/data"):
    os.makedirs("Web-Scraper/data")

# Create logger to log info or errors
logging.basicConfig(
    filename='Web-Scraper/logs/scrapeLogs.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a',
    level=logging.DEBUG)

# Get the absolute path of the directory containing the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Join the script's directory with the filename
config_path = os.path.join(script_dir, 'test_config.json')

# Load the config variables used in the fetcher function. Open the file as 
# read only and extract the variables
with open(config_path, 'r') as file:
    config = json.load(file)

# Set the configs to their proper variable names
location = config['location']
home_type = config['home_type']
price = config['price']

# Get the raw data from the fetcher function and then call the parse function to compile that
# data to be converted into JSON
raw_data = fetcher(location, home_type, price)
compiled_data = parse(raw_data)

def write_data():
    # Turn the compiled data into JSON data
    try:
        house_data = compiled_data
        logging.info(f'Successfully converted data to JSON')
    except ValueError as err:
        logging.error(f'JSON Decode Error: {err}')
        
    # Go up one level from the script's directory
    parent_dir = os.path.dirname(script_dir)

    # Join the parent directory with the 'data' folder and filename
    data_path = os.path.join(parent_dir, 'data', 'house_data.json')

    # This is the final JSON data that will be written to the house_data.json file in the data directory.
    # The key will be a integer with a timestamp, and the value will be the exisitng data
    # First, read the existing data from the file, if any.
    if os.path.exists(data_path):
        with open(data_path, 'r') as infile:
            existing_data = json.load(infile)
    else:
        existing_data = {}

    # Create the new key and assign the house_data to it
    timestamp = datetime.now().strftime('%Y/%m/%d-%H:%M:%S')
    key = f'house_data-{timestamp}' 
    existing_data[key] = house_data

    # Write the combined data back to the file
    try:
        with open(data_path, 'w') as outfile:
            json.dump(existing_data, outfile, indent=4)
            logging.info('Successfully wrote data to file')
    except Exception as err:
        logging.error(f'Error in writing to file: {err}')
    

