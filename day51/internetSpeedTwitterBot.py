from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

URL = "https://x.com/home"
SPEED_URL = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_option)
        driver.get(url=SPEED_URL)
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        time.sleep(2)
        check_button = driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        check_button.click()
        time.sleep(50)
        self.down = driver.find_element(By.XPATH,
                                        '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                        '3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = driver.find_element(By.XPATH,
                                      '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                      '3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self, email, password):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_option)
        self.driver.get(url=URL)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[2]/div/div/div/button').click()
        login_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                '1]/div/div/div[3]/div[4]/a')
        login_button.click()
        time.sleep(5)
        email_text = self.driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
        email_text.send_keys(email)
        time.sleep(3)
        email_text.send_keys(Keys.ENTER)
        time.sleep(40)
        password_text = self.driver.find_element(By.XPATH,
                                                 '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                 '2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div['
                                                 '2]/div[1]/input')
        password_text.send_keys(password)

        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="react-root"]/div/div/div['
                                                       '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                       '1]/div/div/div/div[2]/div['
                                                       '1]/div/div/div/div/div/div/div/div/div/div['
                                                       '1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH,
                                                value='//*[@id="react-root"]/div/div/div['
                                                      '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                      '1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()
