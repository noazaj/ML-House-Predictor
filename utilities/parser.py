"""This file will be used to parse the data fetch in the fetcher.py file. It will take
the HTML contents of the webpage and parse it accordingly."""

import json
from fetcher import fetcher

# Load the config variables used in the fetcher function. Open the file as 
# read only and extract the variables
with open('test_config.json', 'r') as file:
    config = json.load(file)

# Set the configs to their proper variable names
location = config['location']
home_type = config['home_type']
price = config['price']

data = fetcher(location, home_type, price)
