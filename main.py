from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests

def scrape():
      url = 'https://www.walmart.com/'
      response = requests.get(url)
      soup = BeautifulSoup(response.text, 'html.parser')
      print(soup.prettify())

if __name__ == '__main__':
    scrape()