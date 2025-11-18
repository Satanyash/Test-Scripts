from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
sleep(1)
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
sleep(1)
driver.find_element(By.CLASS_NAME, "radius").click()
sleep(1)
print(driver.find_element(By.ID, "flash").text)

driver.quit()