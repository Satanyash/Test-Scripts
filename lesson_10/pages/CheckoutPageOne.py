import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CheckoutPageOne:

    def __init__(self, _driver):
        """
            Эта функция принимает на вход драйвер и ожидает 
            загрузки страницы ввода данных покупателя при 
            создании экземпляра класса
        """
        self.driver = _driver
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Checkout: Your Information']"))
        )

    @allure.step("Ввод имени: {firstname}, фамилии {lastname} и zip-postal кода {zip_postal_code} для покупки")      
    def information(self, firstname: str, lastname: str, zip_postal_code: str):
        """
            Эта функция принимает на вход текстовые значения и 
            вводит данные покупателя в требуемые поля и нажимает 
            кнопку перехода на следующую страницу
        """
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(firstname)
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(lastname)
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(zip_postal_code)
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
        