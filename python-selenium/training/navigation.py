from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

driver.get("https://bandcamp.com/discover/")
print(driver.title)

pagination_button = driver.find_element(By.ID, "view-more")
print(pagination_button.accessible_name)

tracks = driver.find_elements(By.CLASS_NAME, "results-grid-item")
print(len(tracks))
print(tracks[0].text)

track_1 = tracks[0]
album = track_1.find_element(By.CSS_SELECTOR, "div.meta a strong")
print(album.text)

driver.quit()
