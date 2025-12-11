import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class CheckoutPageOne:

    def __init__(self, _driver):
        self.driver = _driver
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Checkout: Your Information']"))
        )

    @allure.step("Ввод данных пользователя для покупки: {firstname}, {lastname}, {zip_postal_code}")      
    def information(self, firstname, lastname, zip_postal_code):
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(firstname)
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(lastname)
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(zip_postal_code)
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
        