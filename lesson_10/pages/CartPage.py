import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, _driver):
        self.driver = _driver
        """
            Эта функция принимает на вход драйвер и 
            ожидает загрузки страницы корзины при 
            создании экземпляра класса
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Your Cart']"))
        )

    @allure.step("Проверка наличия товаров: {buy}")    
    def check_shopping(self, buy: list[str]):
        """
            Эта функция принимает на вход массив с текстовыми 
            значениями наименований товаров и проверяет их 
            наличие на странице корзины
        """
        n = len(buy)
        for i in range(0, n):
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, f"//div[text()='{buy[i]}']")),
            )
        self.driver.find_element(By.ID, "checkout").click()