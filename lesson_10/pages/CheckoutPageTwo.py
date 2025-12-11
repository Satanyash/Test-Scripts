import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CheckoutPageTwo:

    def __init__(self, _driver):
        """
            Эта функция принимает на вход драйвер ожидает 
            загрузки страницы с итоговой суммой к покупке 
            при создании экземпляра класса
        """
        self.driver = _driver
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Checkout: Overview']"))
        )
    
    @allure.step("Фиксация суммы к оплате")  
    def result(self) -> str:
        """
            Эта функция считывает со страницы итоговую 
            сумму к оплате и возвращает ее в виде текста
        """
        result = self.driver.find_element(By.XPATH, f"//div[@class='summary_total_label']").text
        return result