from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# ---------------------------------------------------
# BROWSER SETUP
# ---------------------------------------------------
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

wait = WebDriverWait(driver, 40)

# ---------------------------------------------------
# OPEN ABHIBUS WEBSITE
# ---------------------------------------------------
driver.get("https://www.abhibus.com/")
print("Website opened")

# wait until React fully loads
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

# ---------------------------------------------------
# LOGIN PROCESS
# ---------------------------------------------------
try:
    login_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(),'Login')]")
        )
    )
    login_btn.click()
    print("Login popup opened")

    mobile_input = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='tel']")
        )
    )

    mobile_input.send_keys("9677292876")

    print("Enter OTP manually (30 seconds)...")
    time.sleep(30)

except Exception as e:
    print("Login skipped:", e)

# ---------------------------------------------------
# SEARCH JOURNEY
# ---------------------------------------------------
print("Filling journey details...")

# ---------------- FROM CITY ----------------
from_city = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@placeholder='Leaving From']")
    )
)

from_city.click()
from_city.send_keys("Chennai")

time.sleep(2)
from_city.send_keys(Keys.ARROW_DOWN)
from_city.send_keys(Keys.ENTER)

print("From city selected")

# ---------------- TO CITY ----------------
to_city = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@placeholder='Going To']")
    )
)

to_city.click()
to_city.send_keys("Trichy")

time.sleep(2)
to_city.send_keys(Keys.ARROW_DOWN)
to_city.send_keys(Keys.ENTER)

print("To city selected")

# ---------------- DATE SELECTION ----------------
date_box = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[contains(@placeholder,'Onward')]")
    )
)

date_box.click()

# select first available date
date_select = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//td[not(contains(@class,'disabled'))]/span")
    )
)
date_select.click()

print("Date selected")

# ---------------- SEARCH BUTTON ----------------
search_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(.,'Search')]")
    )
)

search_btn.click()

print("Bus search executed successfully!")

# ---------------------------------------------------
# VIEW RESULTS
# ---------------------------------------------------
time.sleep(20)

driver.save_screenshot("abhibus_result.png")

driver.quit()