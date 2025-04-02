import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("https://bandcamp.com/discover/")

tracks = driver.find_elements(By.CLASS_NAME, "results-grid-item")
print(len(tracks))

pagination_button = driver.find_element(By.ID, "view-more")
pagination_button.click()

time.sleep(0.5)

tracks = driver.find_elements(By.CLASS_NAME, "results-grid-item")
print(len(tracks))

driver.quit()
