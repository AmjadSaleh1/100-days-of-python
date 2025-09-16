from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

URL = "https://login.yahoo.com/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Store the handle of the first window
first_window = driver.current_window_handle
print("First window title = " + driver.title)

# Click the button that opens the second window
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login-body"]/div[1]/div/a[3]'))
)
button.click()

# Wait for the new window to open
sleep(3)  # Adjust this if needed, depending on how fast the new window opens
all_windows = driver.window_handles
print(f"All windows: {all_windows}")

# Switch to the second window (the new one)
driver.switch_to.window(all_windows[-1])
print("Second window title = " + driver.title)

# Now click on the element in the second window
sleep(3)  # Ensure the page is loaded before interacting
driver.find_element(By.XPATH, '//*[@id="menu-secondary-navigation"]/li[2]/a').click()

# Switch back to the first window at the end
driver.switch_to.window(first_window)
sleep(2)  # Add a small delay to ensure the switch takes place
print("Switched back to the first window. Title = " + driver.title)

# Optionally: Refocus the window if needed
driver.switch_to.window(all_windows[-1])
driver.maximize_window()  # Ensures the first window is brought to the front