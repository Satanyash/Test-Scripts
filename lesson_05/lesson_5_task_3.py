from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

driver.find_element(By.CSS_SELECTOR, "input").send_keys("Sky")
sleep(1)
driver.find_element(By.CSS_SELECTOR, "input").clear()
sleep(1)
driver.find_element(By.CSS_SELECTOR, "input").send_keys("Pro")

sleep(1)

driver.quit()