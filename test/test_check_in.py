from pages.login_page import LoginPage
from pages.check_in_pages import CheckInPage
from pages.dashboard_page import DashboardPage
from pages.terminal_page import TerminalPage
from pages.base_page import BasePage


def test_check_in(browser, first_name_data, last_name_data, phone_data, passwd_data):

    login_page = LoginPage(browser)
    login_page.open_check_in_page()
    check_in = CheckInPage(browser)
    check_in.filling_registration_form(first_name_data, last_name_data,
                                       phone_data, passwd_data)
    button_run = DashboardPage(browser)
    button_run.click_button_to_run()
    switch_to_terminal_window = BasePage(browser)
    switch_to_terminal_window.switch_to_terminal_window()
    cheking_button_deposite = TerminalPage(browser)
    cheking_button_deposite.checking_button_deposite()
