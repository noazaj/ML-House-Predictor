"""This file will be used to parse the data fetch in the fetcher.py file. It will take
the HTML contents of the webpage and parse it accordingly."""

import re
import logging

# Configure logger to append to it everytime it is written to
# Might make a small cleanup script for the log to wipe it after a certain time period
logging.basicConfig(
    filename='Web-Scraper/logs/scrapeLogs.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a',
    level=logging.DEBUG)

def extract_location(text):
    match = re.search(r"([\w\s]+, [A-Z]{2})", text)
    if match:
        return match.group(1)
    return None

def houses_data(soup):
    # This will store the data for a house and then for all other houses too
    houses_data = []
    
    house_containers = soup.findAll('div', class_='BasePropertyCard_propertyCardWrap__J0xUj')

    # Using an ordered dict ensures that order is maintained
    for container in house_containers:
        house_dict = {}

        tag_ids = {
            'div': {'card-address': 'address', 
                    'card-price': 'cost'},
            'li': {'property-meta-beds': 'beds',
                   'property-meta-baths': 'baths',
                   'property-meta-sqft': 'sqft',
                   'property-meta-lot-size': 'lot_size'}
        }

        for key, values in tag_ids.items():
            for value, field_name in values.items():
                tag = container.find(key, attrs={"data-testid": value})
                if tag:
                    if value == 'card-address':
                        #s = extract_location(tag.text)
                        s = tag.text
                        house_dict[field_name] = s
                    else:
                        s = re.sub("[^\d]", "", tag.text)
                        house_dict[field_name] = int(s)
        houses_data.append(house_dict)
    return houses_data
    
    

def parse(data: bytes):
    # Import BeautifulSoup and try to catch any errors in the process and log them to the log file
    try:
        from bs4 import BeautifulSoup
        logging.info(f"Successfully imported BeautifulSoup")
    except ImportError as err:
        logging.error('Import error: %s', err)

    # Create the 'soup' from the contents of the HTML data
    soup = BeautifulSoup(data, 'html5lib')
    
    try:
        result = houses_data(soup)
        logging.info(f"Successfully extracted data")
        return result
    except Exception as err:
        logging.error('Extraction error: %s', err)