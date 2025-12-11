import allure
from selenium import webdriver

from pages.CalculatorPage import CalculatorPage

@allure.suite("Тесты калькулятора")
@allure.epic("Калькулятор")
@allure.title("Проверка калькулятора")
@allure.description("Ввод задержки, нажатие кнопок и проверка результата")
@allure.feature("Расчет и проверка результата")
@allure.severity("CRITICAL")
def test_calculator():
    """
        Эта функция тестирует ввод значения в поле
        задержки и проверяет результат расчета через 
        заданное время ожидания
    """
    with allure.step("Запуск браузера Chrome"):
        driver = webdriver.Chrome()
    calculator_page = CalculatorPage(driver)
    calculator_page.delay(1)
    calculator_page.calculate(["7", "+", "8", "="])
    result = calculator_page.result()
    with allure.step("Закрытие браузера"):
        driver.quit()
    with allure.step(f"Проверка правильности результата расчета, равного {result}"):
        assert result == "15"