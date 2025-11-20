import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def calculator(delay, first_number, action, second_number, calc_result):
    result = None
    
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    driver.find_element(By.CSS_SELECTOR, "#delay").clear()
    driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(delay)

    driver.find_element(By.XPATH, f"//div[@class='keys']/span[text()='{first_number}']").click()

    driver.find_element(By.XPATH, f"//div[@class='keys']/span[text()='{action}']").click()

    driver.find_element(By.XPATH, f"//div[@class='keys']/span[text()='{second_number}']").click()

    driver.find_element(By.XPATH, f"//div[@class='keys']/span[text()='=']").click()

    WebDriverWait(driver, delay).until(
        EC.invisibility_of_element_located((By.XPATH, "//p[@class='lead']/span[@id='spinner']"))
    )

    result = driver.find_element(By.XPATH, f"//div[@class='top']/div[@class='screen']").text

    if result == None:
        print("Не удалось получить результат в ожидаемое время")
    else:
        print("Результат получен в ожидаемое время")

    status = False

    if result == None:
        print(f"Результат расчета {result} не равен {calc_result} - провал")
    else:
        result = float(result)
        calc_result = float(calc_result)
        if result == calc_result:
            status = True
            print(f"Результат расчета {result} равен {calc_result} - успех")

    driver.quit()

    return status

@pytest.mark.positive
@pytest.mark.parametrize(
    "delay, first_number, action, second_number, calc_result, expected",
    [
        (45, 7, "+", 8, "15", True),
    ],
)
def test_calculator(delay, first_number, action, second_number, calc_result, expected):
    assert calculator(delay, first_number, action, second_number, calc_result) == expected


