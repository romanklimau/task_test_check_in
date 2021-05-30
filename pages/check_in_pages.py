from pages.base_page import BasePage
from locators.check_in_locators import CheckInPageLocator
from datetime import datetime

class CheckInPage(BasePage):

    email = f"user_ivan{datetime.now().strftime('%d%m%Y_%H_%M_%S')}@ex.com"

    def filling_registration_form(self, first_name, last_name, phone,
                                  password):
        field_first_name = self.find_element(
            CheckInPageLocator.LOCATOR_FIELD_FIRST_NAME
        )
        field_first_name.send_keys(first_name)
        field_last_name = self.find_element(
            CheckInPageLocator.LOCATOR_FIELD_LAST_NAME
        )
        field_last_name.send_keys(last_name)
        field_email = self.find_element(
            CheckInPageLocator.LOCATOR_FIELD_EMAIL
        )
        field_email.send_keys(self.email)
        field_phone = self.find_element(
            CheckInPageLocator.LOCATOR_FIELD_PHONE
        )
        field_phone.send_keys(phone)
        field_password = self.find_element(
            CheckInPageLocator.LOCATOR_FIELD_PASSWORD
        )
        field_password.send_keys(password)
        field_confirm_passwd = self.find_element(
            CheckInPageLocator.LOCATOR_FIELD_CONFIRM_PASSWORD
        )
        field_confirm_passwd.send_keys(password)
        checkbox_agree = self.find_element(
            CheckInPageLocator.LOCATOR_CHECKBOX_AGREE_WITH_THE_TERMS
        )
        checkbox_agree.click()
        button_check_in = self.find_element(
            CheckInPageLocator.LOCATOR_BUTTON_CHECK_IN
        )
        button_check_in.click()
