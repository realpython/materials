import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()  # Run in normal mode
driver.get("https://bandcamp.com/discover/")

# Accept cookies, if required
try:
    cookie_accept_button = driver.find_element(
        By.CSS_SELECTOR,
        "#cookie-control-dialog button.g-button.outline",
    )
    cookie_accept_button.click()
except NoSuchElementException:
    pass

time.sleep(0.5)

search = driver.find_element(By.CLASS_NAME, "site-search-form")
search_field = search.find_element(By.TAG_NAME, "input")
search_field.send_keys("selenium")
search_field.submit()

time.sleep(5)

driver.quit()
