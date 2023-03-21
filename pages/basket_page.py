from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_message(self):
        empty_notification = "Your basket is empty."
        assert empty_notification in self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text, 'There is no ' \
            'corresponding message! '

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PROCEED_BUTTON), 'The button is on the page!'

    def no_empty_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_MESSAGE), "The message is present!"

    def should_be_checkout_button(self):
        assert self.is_element_present(*BasketPageLocators.PROCEED_BUTTON), "The button is absent!"
