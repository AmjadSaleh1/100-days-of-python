import os

from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ["MY_EMAIl"]
PASSWORD = os.environ["MY_PASSWORD"]
URL = ("https://www.amazon.com/dp/B079C6W98L/ref=syn_sd_onsite_desktop_0?ie=UTF8&psc=1&pf_rd_p=d77a94d7-221a-4129-af34"
       "-3c16ad136bb7&pf_rd_r=FSG2AKCPHZSMT08XSWGM&pd_rd_wg=LIPiP&pd_rd_w=cVZgK&pd_rd_r=e7154278-42ac-4861-8f8b"
       "-e83b8dfbac7a&aref=blwEMtB2fT")
TARGET_PRICE = 100.00

paramter = {
    "Accept-Language": "he,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,fr;q=0.6,ar;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 "
                  "Safari/537.36 Edg/129.0.0.0",

}

response = requests.get(URL, headers=paramter)

soup = BeautifulSoup(response.text, 'lxml')
print(soup.prettify())
price = soup.find("span", class_="a-offscreen")
before_strip = price.getText().split('$')[1]
after_strip = before_strip.strip('\u200e')
pricew = after_strip
price_as_float = float(pricew)
print(price_as_float)

if price_as_float < TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="amjadsalih1809@gmail.com",
            msg=f"Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, now {price_as_float}"
        )
