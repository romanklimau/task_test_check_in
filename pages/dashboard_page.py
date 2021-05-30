from pages.base_page import BasePage
from locators.dashboard_locators import DashboardPageLocator

class DashboardPage(BasePage):

    def click_button_to_run(self):
        button_run = self.find_element(
            DashboardPageLocator.LOCATOR_BUTTON_RUN
        )
        button_run.click()
