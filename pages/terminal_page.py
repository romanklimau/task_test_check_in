from pages.base_page import BasePage
from locators.terminal_locators import TerminalPageLocator


class TerminalPage(BasePage):

    def checking_button_deposite(self):
        button_deposite = self.find_element(
            TerminalPageLocator.LOCATOR_ACCOUNT_TEXT
        )
        assert button_deposite != 0,\
            f'{button_deposite} is not found!!!'
