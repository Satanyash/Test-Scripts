import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ShoppingPage:
 
    def __init__(self, _driver):
        """
            Эта функция принимает на вход драйвер и ожидает 
            загрузки главной страницы с товарами при создании 
            экземпляра класса
        """
        self.driver = _driver
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Products']"))
        )

    @allure.step("Добавление товаров в корзину: {buy}")  
    def shopping(self, buy: list[str]):
        """
            Эта функция принимает на вход массив с текстовыми 
            наименованиями товаров, ищет их на странице и 
            добавляет в корзину
        """
        n = len(buy)
        for i in range(0, n):
            self.driver.find_element(By.XPATH, f"//div[text()='{buy[i]}']").click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "back-to-products"))
            )
            self.driver.find_element(By.ID, "add-to-cart").click()
            self.driver.back()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//span[text()='Products']"))
            )
    
    @allure.step("Переход в корзину")  
    def go_to_cart(self):
        """
            Эта функция нажимает кнопку перехода на
            страницу корзины
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        