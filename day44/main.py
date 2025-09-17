from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://appbrewery.github.io/gym/"

edge_option = webdriver.EdgeOptions
edge_option.add_experimental_option("detach", True)

