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

def parse(data: bytes):
    # Import BeautifulSoup and try to catch any errors in the process and log them to the log file
    try:
        from bs4 import BeautifulSoup
        logging.info(f"Successfully imported BeautifulSoup")
    except ImportError as err:
        logging.error('Import error: %s', err)

    # Create the 'soup' from the contents of the HTML data
    soup = BeautifulSoup(data, 'html5lib')

    # Parse the specific content of the webpage to return the data-testid attribute
    try:
        table = soup.findAll('div', attrs={"data-testid": "card-price"})
        logging.info(f"Successfully extracted data")
    except Exception as err:
        logging.error('Extraction error: %s', err)

    # With the data extracted, now we must iterate over the table to add the pricing value
    # to the house_prices list
    house_dict = {}
    for i, row in enumerate(table):
        s = row.text
        tmp_str = re.sub("[From$,]", "", s)
        house_dict[i] = int(tmp_str)
    return house_dict