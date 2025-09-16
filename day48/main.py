from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/Main_Page"

#keep the browser open
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(URL)

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"the price is {price_dollar.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar)


# even_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# even_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# events_dic = {}
#
# for n in range(len(even_times)):
#     events_dic[n] = {
#         "time": even_times[n].text,
#         "name": even_names[n].text,
#     }
# print(events_dic)


driver.quit()
