from selenium import webdriver
from time import sleep

from pages.LoginPage import LoginPage
from pages.ShoppingPage import ShoppingPage   
from pages.CartPage import CartPage
from pages.CheckoutPageOne import CheckoutPageOne
from pages.CheckoutPageTwo import CheckoutPageTwo

def test_shopping():
    driver = webdriver.Edge()
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
    driver.quit()
    assert result == "Total: $58.29"