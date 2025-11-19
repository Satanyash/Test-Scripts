from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#landscape"))
)

print(driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src"))

driver.quit()