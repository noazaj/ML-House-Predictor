"""This file will be used to fetch the webpage data. It will open the website and get the contents
of the webpage. It will not parse the webpage though."""

from urllib.request import urlopen

# This function will take the website/webpage URL and fetch it
def fetcher(url):
    page = urlopen(url)
    






# Test function
test1 = "http://olympus.realpython.org/profiles/aphrodite"
fetcher(test1)