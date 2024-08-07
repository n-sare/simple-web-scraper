import requests
from bs4 import BeautifulSoup
import time

def create_session():
    return requests.Session()

# Function to check for the word 'motherfucking' on the page
def check_word_in_page(session, url, word):
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Debug: print a portion of the page content
    print(f'Page content snippet: {soup.text[:500]}')
    if word.lower() in soup.text.lower():
        return True
    return False

# URL and word to search
target_url = 'https://thebestmotherfucking.website/'
word_to_search = 'motherfucking'

# Create a session
session = create_session()

# Monitoring the page
while True:
    if check_word_in_page(session, target_url, word_to_search):
        print(f"The word '{word_to_search}' was found on the page {target_url}.")
        break
    time.sleep(3600)  # Check every hour
