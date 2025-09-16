from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://orteil.dashnet.org/experiments/cookie/"

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(URL)
# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()
# all_portals = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a/span[1]')
# all_portals.click()
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

# fname = driver.find_element(By.NAME, value="fName")
# fname.send_keys("amjad")
# lname = driver.find_element(By.NAME, value="lName")
# lname.send_keys("salih")
# eadress = driver.find_element(By.NAME, value="email")
# eadress.send_keys("as@gmail.com")
# sign = driver.find_element(By.CSS_SELECTOR, value=".text-center button")
# sign.click()


clicking = driver.find_element(By.ID, value="cookie")
clicking.click()
clicking.click()
clicking.click()
clicking.click()
clicking.click()
money = driver.find_element(By.ID, value="money")
print(int(money.text))
# driver.quit()
