"""This file will be used to fetch the webpage data. It will open the website and get the contents
of the webpage. It will not parse the webpage though."""

import requests
import time
import logging
import os
import sys

if not os.path.exists("webScraper/logs"):
    os.makedirs("webScraper/logs")

# Configure logger to append to it everytime it is written to
# Might make a small cleanup script for the log to wipe it after a certain time period
logging.basicConfig(
    filename='webScraper/logs/scrapeLogs.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a',
    level=logging.DEBUG)

def fetcher(location: str, home_type=None, price=None) -> bytes:
    base_url = "https://www.realtor.com/realestateandhomes-search/"

    # Append the location onto the base_url. There needs to be a location in order
    # for the fetch to work
    url = base_url + f'{location}/'


    # If there was a home_type parameter passed, append it to the URL
    # If there was a price parameter passed, also append it to the URL
    if home_type:
        url += f'{home_type}/'
    if price:
        url += f'{price}/'
    
    # Use header agent to simulate the request as a browser and not the default request method
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Get the response from the GET request for the URL provided. There are only 3 attempts before
    # the loop breaks. The code within the loop will run the request and catch and exceptions it throws
    # and log them to a file.
    i, max_tries = 0, 3
    while i < max_tries:
        try:
            response = requests.get(url, headers=headers)
            logging.info(f"Successfully fetched data from {url}")
            break
        except requests.exceptions.HTTPError as err:
            logging.exception('HTTP Error: %s', err)
            i += 1
            print(f'HTTP Error -> {err}')
            time.sleep(7)
        except requests.exceptions.Timeout as err:
            logging.error('Timeout error: %s', err)
            i += 1
            print(f'Timeout Error -> {err}')
            time.sleep(7)
        except requests.exceptions.TooManyRedirects as err:
            logging.error('Too many redirects error: %s', err)
            i += 1
            print(f'Too many redirects -> {err}')
            time.sleep(7)
        except requests.exceptions.RequestException as err:
            logging.critical('Critical error: %s', err)
            print(f'Critical Error -> {err}')
            sys.exit()

    if response.status_code != 200:
        print(f'Error {response.status_code}: Unable to fetch webpage')
    else:
        html_content = response.content
        return html_content