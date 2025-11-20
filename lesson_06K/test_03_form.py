import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def shopping(username, password, buy1, buy2, buy3, firstname, lastname, zip_postal_code, sum):
    result = None
    
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.CSS_SELECTOR, "#user-name").clear()
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(username)

    driver.find_element(By.CSS_SELECTOR, "#password").clear()
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)

    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    
    driver.find_element(By.XPATH, f"//div[@class='inventory_item_label']//div[text()='{buy1}']").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart").click()
    driver.back()
    driver.find_element(By.XPATH, f"//div[@class='inventory_item_label']//div[text()='{buy2}']").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart").click()
    driver.back()
    driver.find_element(By.XPATH, f"//div[@class='inventory_item_label']//div[text()='{buy3}']").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart").click()
    driver.back()

    driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()

    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    driver.find_element(By.CSS_SELECTOR, "#first-name").clear()
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(firstname)

    driver.find_element(By.CSS_SELECTOR, "#last-name").clear()
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(lastname)

    driver.find_element(By.CSS_SELECTOR, "#postal-code").clear()
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(zip_postal_code)

    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    result = driver.find_element(By.XPATH, f"//div[@class='summary_total_label']").text

    status = False

    print(result)

    if result == sum:
        status = True
        print("{result} - успех")

    driver.quit()

    return status

@pytest.mark.positive
@pytest.mark.parametrize(
    "username, password, buy1, buy2, buy3, firstname, lastname, zip_postal_code, sum, expected",
    [
        ("standard_user", 
        "secret_sauce", 
        "Sauce Labs Backpack", 
        "Sauce Labs Bolt T-Shirt", 
        "Sauce Labs Onesie", 
        "Satyam",
        "Fedorov",
        "1245",
        "Total: $58.29",
        True),
    ],
)
def test_shopping(username, password, buy1, buy2, buy3, firstname, lastname, zip_postal_code, sum, expected):
    assert shopping(username, password, buy1, buy2, buy3, firstname, lastname, zip_postal_code, sum) == expected


