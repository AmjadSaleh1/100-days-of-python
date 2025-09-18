from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

booked_count = 0
waitlist_count = 0
already_booked_count = 0

URL = "https://appbrewery.github.io/gym/"

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Edge(options=chrome_option)
wait = WebDriverWait(driver, 10)

#entering the website and logging in.
driver.get(URL)
login_button = driver.find_element(By.CLASS_NAME, value="Navigation_button__uyKX2")
login_button.click()
email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email-input"]')))
email_input.send_keys("student@test.com")
password_input = driver.find_element(By.XPATH, value='//*[@id="password-input"]')
password_input.send_keys("password123")
submit_button = driver.find_element(By.CLASS_NAME, value="Login_submitButton__tJFna ")
submit_button.click()

#start booking
sleep(5)

schedule_div = driver.find_element(By.XPATH, '//*[@id="schedule-page"]')
day_groups = schedule_div.find_elements(By.CLASS_NAME, "Schedule_dayGroup__y79__")

#booking all tue and sat 6 pm classes.
for card in day_groups:
    day_title = card.find_element(By.TAG_NAME, "h2").text

    if "Tue," in day_title or "Sat," in day_title:
        for time in card.find_elements(By.CLASS_NAME, "ClassCard_classDetail__Z8Z8f"):
            time_text = time.text
            if "6:00 PM" in time_text:
                button = card.find_element(By.TAG_NAME, "button")
                if button.text == "Booked":
                    already_booked_count += 1
                    print("already booked")
                    break

                if button.text == "Waitlisted":
                    print("u are on the waitlist")
                    already_booked_count += 1

                if button.text == "Join Waitlist":
                    button.click()
                    waitlist_count += 1
                    print("you joined to the waitlist")
                    break

                else:
                    button.click()
                    booked_count += 1
                    print("Clicked!")
                    break

my_booking_page = driver.find_element(By.ID, value="my-bookings-link")
my_booking_page.click()
sleep(3)

booked_cards = driver.find_elements(By.CSS_SELECTOR, "#confirmed-bookings-section > div > "
                                                     "div.MyBookings_bookingCard__VRdrR")
all_classes_count = 0
for c in booked_cards:
    if "Tue" in c.text or "Sat" in c.text:
        all_classes_count += 1

print("\n--- BOOKING SUMMARY ---")
print(f"Classes booked: {booked_count}")
print(f"Waitlists joined: {waitlist_count}")
print(f"Already booked/waitlisted: {already_booked_count}")
print(f"Total Tuesday 6pm classes processed: {booked_count + waitlist_count + already_booked_count}")
print(f"Total booked for Tuesday and Saturday Classes: {all_classes_count}")
