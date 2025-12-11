import allure
from selenium import webdriver

from pages.LoginPage import LoginPage
from pages.ShoppingPage import ShoppingPage   
from pages.CartPage import CartPage
from pages.CheckoutPageOne import CheckoutPageOne
from pages.CheckoutPageTwo import CheckoutPageTwo

@allure.title("Проверка магазина")
@allure.description("Авторизация, добавление товаров в корзину, ввод информации покупателя и проверка итоговой суммы")
@allure.feature("Авторизация, покупка и проверка результата")
@allure.severity("critical")
def test_shopping():
    with allure.step("Запуск браузера Edge"):
        driver = webdriver.Edge()
    with allure.step("Отметка товаров для покупки"):
        buy = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    shopping_page = ShoppingPage(driver)
    shopping_page.shopping(buy)
    shopping_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.check_shopping(buy)
    checkout_page_one = CheckoutPageOne(driver)
    checkout_page_one.information("Satyam", "Fedorov", "123")
    checkout_page_two = CheckoutPageTwo(driver)
    result = checkout_page_two.result()
    with allure.step("Закрытие браузера"):
        driver.quit()
    with allure.step("Проверка соответствия итоговой суммы"):
        assert result == "Total: $58.29"