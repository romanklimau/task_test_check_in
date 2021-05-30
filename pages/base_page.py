from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: tuple, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f'can not find locator: {locator}')

    def switch_to_terminal_window(self):
        id_windows_now = self.driver.current_window_handle
        list_id_window = self.driver.window_handles
        index_id = list_id_window.index(id_windows_now)
        del list_id_window[index_id]
        self.driver.switch_to.window(list_id_window[0])
