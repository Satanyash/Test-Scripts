import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CalculatorPage:

    @allure.step("Открытие страницы с калькулятором")
    def __init__(self, _driver):
        """
            Эта функция принимает на вход драйвер, открывает главную 
            страницу с калькулятором и ожидает загрузки страницы 
            при создании экземпляра класса
        """
        self.driver = _driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[text()='Slow calculator']"))
        )

    @allure.step("Ввод значения задержки {_delay}с")
    def delay(self, _delay: int):
        """
            Эта функция принимает на вход целочисленное 
            значение задержки и вводит его в требуемое поле
        """
        self.delay = _delay
        self.driver.find_element(By.CSS_SELECTOR, "input[type='text']").clear()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(self.delay)

    @allure.step("Ввод выражения {button}")
    def calculate(self, button: list[str]):
        """
            Эта функция принимает на вход массив с текстовыми 
            значениями, представляющий собой выражение, которое 
            необходимо расчитать, и нажимает на требуемые кнопки
        """
        n = len(button)
        for i in range(0, n):
            self.driver.find_element(By.XPATH, f"//span[text()='{button[i]}']").click()
        self.calc = self.driver.find_element(By.CLASS_NAME, "screen").text

    @allure.step("Фиксация результата расчета")   
    def result(self) -> str:
        """
            Эта функция возвращает результат расчета после 
            задержки в виде текста
        """
        WebDriverWait(self.driver, self.delay).until(
            EC.none_of(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), self.calc)
            )
        )
        result = self.driver.find_element(By.CLASS_NAME, "screen").text
        return result