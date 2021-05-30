from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocator

class LoginPage(BasePage):

    def open_check_in_page(self):
        button_check_in = self.find_element(
            LoginPageLocator.LOCATOR_BUTTON_CHECK_IN
        )
        button_check_in.click()
