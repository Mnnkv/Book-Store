from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def product_added(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart.click()
        self.solve_quiz_and_get_code()
        product_name_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_CART).text
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL).text
        assert product_name == product_name_cart, "Product name is wrong!"
        assert product_price == total_price, "Price is wrong!"

    def product_added_no_math(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart.click()
        product_name_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_CART).text
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL).text
        assert product_name == product_name_cart, "Product name is wrong!"
        assert product_price == total_price, "Price is wrong!"

    def just_add_product(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message hasn't disappeared"







