from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class CalculatorPage:

    def __init__(self, _driver):
        self.driver = _driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[text()='Slow calculator']"))
        )


    def delay(self, _delay):
        self.delay = _delay
        self.driver.find_element(By.CSS_SELECTOR, "input[type='text']").clear()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(self.delay)

    def calculate(self, button):
        n = len(button)
        for i in range(0, n):
            self.driver.find_element(By.XPATH, f"//span[text()='{button[i]}']").click()
        self.calc = self.driver.find_element(By.CLASS_NAME, "screen").text
    
    def result(self):
        WebDriverWait(self.driver, self.delay).until(
            EC.none_of(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), self.calc)
            )
        )
        result = self.driver.find_element(By.CLASS_NAME, "screen").text
        return result