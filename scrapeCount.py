import requests
from bs4 import BeautifulSoup

def get_site_text(url, word):
    '''
    Get the text from a website

    Parameters
    ----------  
    url : str
        The url of the website to scrape

    Returns
    -------
    str
        The text from the website
    '''
    # Get the website
    response = requests.get(url)

    # Raise exception for unsuccessful status codes
    response.raise_for_status()

    # Parse the website
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the text
    text = soup.get_text()

    # Count the number of times the word appears
    count = text.count(word)

    return count

# User inputted URL
url = input('Enter a website to scrape: ')

# Preprocess the URL
if not url.startswith('http'):
    url = 'http://' + url

# User inputted word
word = input('Enter a word to count: ')

print(get_site_text(url, word))