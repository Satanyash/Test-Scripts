from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

element = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
)

print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)

driver.quit()