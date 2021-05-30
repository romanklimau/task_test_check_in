from selenium.webdriver.common.by import By


class CheckInPageLocator:
    LOCATOR_FIELD_FIRST_NAME = (By.XPATH, '//input[@name="first_name"]')
    LOCATOR_FIELD_LAST_NAME = (By.XPATH, '//input[@name="last_name"]')
    LOCATOR_FIELD_EMAIL = (By.XPATH, '//input[@name="email"]')
    LOCATOR_FIELD_PHONE = (By.XPATH, '//input[@name="phone"]')
    LOCATOR_FIELD_PASSWORD = (By.XPATH, '//input[@name="password"]')
    LOCATOR_FIELD_CONFIRM_PASSWORD = (By.XPATH,
                                      '//input[@name="password_confirmation"]')
    LOCATOR_CHECKBOX_AGREE_WITH_THE_TERMS = (By.XPATH,
                                             "//input[@type='checkbox']")
    LOCATOR_BUTTON_CHECK_IN = (By.XPATH, '//div[@class="flex items-center'
                                         ' justify-end mt-4"]/button')
