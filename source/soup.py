import requests
from bs4 import BeautifulSoup

def return_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup