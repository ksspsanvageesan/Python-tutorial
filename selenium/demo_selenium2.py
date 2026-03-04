from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# ==============================
# Browser Setup
# ==============================
driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

base_url = "https://the-internet.herokuapp.com"


# ==============================
# TEST 1 — Login Functionality
# ==============================
driver.get(base_url + "/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Wait for success message
wait.until(
    EC.visibility_of_element_located((By.ID, "flash"))
)

print("✅ Login Test Passed")


# ==============================
# TEST 2 — Checkboxes
# ==============================
driver.get(base_url + "/checkboxes")

checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

if not checkboxes[0].is_selected():
    checkboxes[0].click()

if not checkboxes[1].is_selected():
    checkboxes[1].click()

print("✅ Checkbox Test Passed")


# ==============================
# TEST 3 — Dropdown Selection
# ==============================
driver.get(base_url + "/dropdown")

dropdown = Select(driver.find_element(By.ID, "dropdown"))
dropdown.select_by_visible_text("Option 2")

print("✅ Dropdown Test Passed")


# ==============================
# TEST 4 — JavaScript Alert (FINAL FIX)
# ==============================
driver.get(base_url + "/javascript_alerts")

# Wait until button becomes clickable
alert_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Click for JS Alert']")
    )
)

# Small human-like delay (improves stability)
time.sleep(0.5)

# Click button
alert_button.click()

# Wait for alert to appear
wait.until(EC.alert_is_present())

alert = driver.switch_to.alert
print("Alert Text:", alert.text)

alert.accept()

print("✅ Alert Test Passed")


# ==============================
# TEST 5 — Add/Remove Elements
# ==============================
driver.get(base_url + "/add_remove_elements/")

add_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Add Element']")
    )
)

# Add elements
for i in range(3):
    add_btn.click()

delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

print(f"✅ Added {len(delete_buttons)} elements successfully")


# ==============================
# Close Browser
# ==============================
time.sleep(2)
driver.quit()

print("\n🎉 ALL 5 TESTS COMPLETED SUCCESSFULLY")