"""This file will be used to parse the data fetch in the fetcher.py file. It will take
the HTML contents of the webpage and parse it accordingly."""

import json
import re
import logging
import os
from fetcher import fetcher

# Configure logger to append to it everytime it is written to
# Might make a small cleanup script for the log to wipe it after a certain time period
logging.basicConfig(
    filename='webScraper/logs/scrapeLogs.log',
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

raw_data = fetcher(location, home_type, price)

def parse(data: bytes):
    # Import BeautifulSoup and try to catch any errors in the process and log them to the 
    # log file
    try:
        from bs4 import BeautifulSoup
        logging.info(f"Successfully imported BeautifulSoup")
    except ImportError as err:
        logging.error('Import error: %s', err)

    # Create the 'soup' from the contents of the HTML data
    soup = BeautifulSoup(data, 'html5lib')
    
    # A list to store all the house prices
    house_data = []

    # Parse the specific content of the webpage to return the data-testid attribute
    try:
        table = soup.findAll('div', attrs={"data-testid": "card-price"})
        logging.info(f"Successfully extracted data")
    except Exception as err:
        logging.error('Extraction error: %s', err)

    # With the data extracted, now we must iterate over the table to add the pricing value
    # to the house_prices list
    for i, row in enumerate(table):
        s = row.text
        tmp_str = re.sub("[$,]", "", s)
        dict = {
            i: int(tmp_str)
        }
        house_data.append(dict)
    print(house_data)

# Test function
parse(raw_data)