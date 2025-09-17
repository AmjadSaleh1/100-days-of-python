from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from time import sleep

URL = "https://appbrewery.github.io/gym/"

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Edge(options=chrome_option)
wait = WebDriverWait(driver, 10)

driver.get(URL)
login_button = driver.find_element(By.CLASS_NAME, value="Navigation_button__uyKX2")
login_button.click()
email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email-input"]')))
email_input.send_keys("student@test.com")
password_input = driver.find_element(By.XPATH, value='//*[@id="password-input"]')
password_input.send_keys("password123")
submit_button = driver.find_element(By.CLASS_NAME, value="Login_submitButton__tJFna ")
submit_button.click()

sleep(5)
day_title = driver.find_element(By.XPATH, '//*[@id="day-title-tue,-sep-23"]')
day_div = day_title.find_element(By.XPATH, './..')

for card in day_div.find_elements(By.CLASS_NAME, "ClassCard_card__qx5"):
    class_time = card.find_element(By.CLASS_NAME, "ClassCard_classDetail__Z8Z8f").text

    if "9:00 AM" in class_time:
        button = card.find_element(By.TAG_NAME, "button")
        button.click()
        print("Clicked!")
        break
