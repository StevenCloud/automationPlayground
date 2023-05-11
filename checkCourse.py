import requests
from bs4 import BeautifulSoup

def get_site_text(url):
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

    # Find the index of the string Section Max Enrollment: and Section Enrolled:
    indexMax = text.find('Section Max Enrollment:')
    indexEnrolled = text.find('Section Enrolled:')

    # Get the substring after the string Section Max Enrollment: and Section Enrolled:
    substringMax = text[indexMax + len('Section Max Enrollment:'):]
    substringEnrolled = text[indexEnrolled + len('Section Enrolled:'):]

    # Get the first word in the string
    numMax = substringMax.split()[0]
    numEnrolled = substringEnrolled.split()[0]

    #Remove any non integer from text
    numMax = ''.join([char for char in numMax if char.isdigit()])
    numEnrolled = ''.join([char for char in numEnrolled if char.isdigit()])

    #Convert text to integer
    numMax = int(numMax)
    numEnrolled = int(numEnrolled)

    if (numMax > numEnrolled):
        returnText = 'There is space in the class'
    else:
        returnText = 'There is no space in the class'

    return returnText

#User inputted URL
url = input('Enter a website to scrape: ')

# Preprocess the URL
if not url.startswith('http'):
    url = 'http://' + url

print(get_site_text(url))