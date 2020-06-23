import logging
import utilities.custom_logger as cl
from selenium.webdriver.common.by import By
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage


class LoginPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = 'Login'
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = 'commit'
    _user_icon = 'gravatar'
    _invalid_login = 'Invalid email or password.'
    _logout_link = 'user-signout'

    # Actions
    def click_login_link(self):
        self.element_click(self._login_link, locator_type='link')

    def enter_email(self, email):
        self.send_data(email, self._email_field)
        # self.get_email_field().send_keys(email)

    def enter_password(self, password):
        self.send_data(password, self._password_field)
        # self.get_password_field().send_keys(password)

    def click_login_button(self):
        self.element_click(self._login_button, locator_type='name')
        # self.get_login_button().click()

    def clear_fields(self):
        email_field = self.get_element(self._email_field)
        email_field.clear()
        password_field = self.get_element(self._password_field)
        password_field.clear()

    # Login method
    def login(self, email='', password=''):
        self.click_login_link()
        self.clear_fields()
        self.enter_email(email)
        self.enter_password(password)
        # time.sleep(1)
        self.click_login_button()

    def verify_login_successful(self):
        return self.is_element_present(self._user_icon, locator_type='class')
        # user_icon = driver.find_element(By.CLASS_NAME, 'gravatar')

    def verify_login_failed(self):
        return self.is_element_present(self._invalid_login, locator_type='link')

    def logout(self):
        # self.element_click(self._user_icon, locator_type='class')
        self.nav.navigate_to_user_icon()
        self.element_click(self._logout_link, locator_type='class')

    def verify_login_title(self):
        # return self.verify_page_title('Google')
        if 'Let\'s Kode It' in self.get_title():
            return True
        else:
            return False
