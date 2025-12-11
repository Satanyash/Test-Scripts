import allure
from selenium import webdriver

from pages.CalculatorPage import CalculatorPage

@allure.title("Проверка калькулятора")
@allure.description("Ввод задержки, нажатие кнопок и проверка результата")
@allure.feature("Расчет и проверка результата")
@allure.severity("Medium")
def test_calculator():
    with allure.step("Запуск браузера Chrome"):
        driver = webdriver.Chrome()
    calculator_page = CalculatorPage(driver)
    calculator_page.delay(1)
    calculator_page.calculate(["7", "+", "8", "="])
    result = calculator_page.result()
    with allure.step("Закрытие браузера"):
        driver.quit()
    with allure.step("Проверка правильности рассчитанного значения"):
        assert result == "15"