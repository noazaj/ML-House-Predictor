"""This file will be used to parse the data fetch in the fetcher.py file. It will take
the HTML contents of the webpage and parse it accordingly."""

import json
import os
from fetcher import fetcher

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

data = fetcher(location, home_type, price)

def parse():
    pass
