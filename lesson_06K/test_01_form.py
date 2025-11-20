import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def form_is_right(values):
    parameters = [
    "first-name", 
    "last-name", 
    "address", 
    "e-mail",
    "phone", 
    "zip-code", 
    "city", 
    "country",
    "job-position",
    "company"
    ]

    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    for i in range(0, 10):
        driver.find_element(By.XPATH, f"//*[@name='{parameters[i]}']").send_keys(values[i])

    driver.find_element(By.CLASS_NAME, "btn-outline-primary").click()

    status = True

    for i in range(0, 10):
        x = driver.find_element(By.CSS_SELECTOR, f"#{parameters[i]}").get_attribute("class")
        if x == "alert py-2 alert-danger":
            status = False
            print(f"Поле {parameters[i]} - подсвечено красным")
        else:
            print(f"Поле {parameters[i]} - подсвечено зеленым")

    driver.quit()

    return status

@pytest.mark.parametrize(
    "values, expected",
    [
        ([
            "Иван",
            "Петров",
            "Ленина, 55-3",
            "test@skypro.com",
            "+7985899998787",
            "",
            "Москва",
            "Россия",
            "QA",
            "SkyPro"
        ], False),
    ],
)
def test_form_is_right(values, expected):
    assert form_is_right(values) == expected


