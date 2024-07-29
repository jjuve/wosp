from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome()

sleep(5)

driver.get("https://app.wodify.com/")

sleep(5)

driver.quit()

def scrape():
      url = 'https://app.wodify.com/'
      response = requests.get(url)
      soup = BeautifulSoup(response.text, 'html.parser')
      print(soup.prettify())

if __name__ == '__main__':
    scrape()