from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

import time




chrome_options = Options()
chrome_options.add_argument("--mute-audio")
# chrome_options.add_argument("--disable-gpu") 
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://millionpoints.chase.com/?pg_name=entry')
wait = WebDriverWait(driver, 10)

time.sleep(10)

dropdown = driver.find_element("id", "edit-field-card")
select = Select(dropdown)
select.select_by_visible_text("Ink Business Preferred®")
time.sleep(3)

input_field = driver.find_element("id", "edit-field-vendor-token-0-value")
input_field.send_keys("4529")
time.sleep(3)

first_name_field = driver.find_element("id", "edit-field-name-first-0-value")
first_name_field.send_keys("Alan")
time.sleep(3)

last_name_field = driver.find_element("id", "edit-field-name-last-0-value")
last_name_field.send_keys("Zhang")
time.sleep(3)

phone_field = driver.find_element("id", "edit-field-phone-0-value")
phone_field.send_keys("7754400229")
time.sleep(3)

email_field = driver.find_element("id", "edit-field-email-0-value")
email_field.send_keys("alanzhang2021@gmail.com")
time.sleep(3)


checkbox = driver.find_element("id", "edit-field-rules-consent-value")
if not checkbox.is_selected():
    checkbox.click()
time.sleep(3)

checkbox = driver.find_element("id", "edit-field-age-confirm-value")
if not checkbox.is_selected():
    checkbox.click()
time.sleep(5)


submit_button = driver.find_element("id", "submit-entry")
submit_button.click()

time.sleep(10)