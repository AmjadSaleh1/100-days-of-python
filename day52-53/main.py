from bs4 import BeautifulSoup
import lxml
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

FORM_URL = ("https://docs.google.com/forms/d/e/1FAIpQLScEezGfTcyVobOD0zKimppawEElUtgqpLKDjSHM1JcnRyyayw/viewform?usp"
            "=sf_link")

ZOLON_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(ZOLON_URL)

soup = BeautifulSoup(response.text, "lxml")
list_of_hotels = soup.find("ul", class_="List-c11n-8-84-3-photo-cards")
# print(list_of_hotels)
links_for_the_hotel = []
list_of_prices = []
list_of_address = []

#get all the links
for a in list_of_hotels.find_all('a', href=True):
    links_for_the_hotel.append(a['href'])

#get all the prices.
for price in list_of_hotels.find_all('span', class_="PropertyCardWrapper__StyledPriceLine"):
    price_before_split = price.text
    price_after_split = re.split(r'[+/]', price_before_split)
    list_of_prices.append(price_after_split[0])

#get all address
for address in list_of_hotels.find_all('address'):
    list_of_address.append(re.sub(r'\s+', ' ', address.text).strip())

#updating form
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
driver.get(url=FORM_URL)
time.sleep(2)

#sending all the information to the form .
for i in range(len(list_of_address)):
    address_answer = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="i1"]')
    price_answer = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="i5"]')
    link_answer = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="i9"]')
    address_answer.send_keys(list_of_address[i])
    price_answer.send_keys(list_of_prices[i])
    link_answer.send_keys(links_for_the_hotel[i])
    send_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    send_button.click()
    new_form_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    new_form_button.click()
    time.sleep(4)
