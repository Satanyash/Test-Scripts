from selenium import webdriver
from time import sleep

from pages.CalculatorPage import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome()
    calculator_page = CalculatorPage(driver)
    calculator_page.delay(45)
    calculator_page.calculate(["7", "+", "8", "="])
    result = calculator_page.result()
    driver.quit()
    assert result == "15"