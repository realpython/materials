from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(5)

driver.get("https://bandcamp.com/discover/")

tracks = driver.find_elements(By.CLASS_NAME, "results-grid-item")
print(len(tracks))

try:
    cookie_accept_button = driver.find_element(
        By.CSS_SELECTOR,
        "div.cookie-control button.g-button.outline",
    )
    cookie_accept_button.click()
except NoSuchElementException:
    pass

wait = WebDriverWait(driver, 10)

pagination_button = wait.until(
    EC.element_to_be_clickable((By.ID, "view-more"))
)
pagination_button.click()

wait.until(EC.element_to_be_clickable((By.ID, "view-more")))

tracks = driver.find_elements(By.CLASS_NAME, "results-grid-item")
print(len(tracks))

driver.quit()
