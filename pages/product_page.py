from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def product_added(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart.click()
        self.solve_quiz_and_get_code()
        #self.browser.find_element(*ProductPageLocators.CART).click()
        product_name_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_CART).text
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL).text
        assert product_name == product_name_cart, "Product name is wrong!"
        assert product_price == total_price, "Price is wrong!"






