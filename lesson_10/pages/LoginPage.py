import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:

    @allure.step("Открытие страницы авторизации")  
    def __init__(self, _driver):
        self.driver = _driver
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Swag Labs']"))
        )

    @allure.step("Авторизация с данными пользователя: {username}, {password}")  
    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#password").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    