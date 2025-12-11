import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CheckoutPageTwo:

    def __init__(self, _driver):
        self.driver = _driver
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Checkout: Overview']"))
        )
    
    @allure.step("Фиксация суммы к оплате")  
    def result(self):
        result = self.driver.find_element(By.XPATH, f"//div[@class='summary_total_label']").text
        return result