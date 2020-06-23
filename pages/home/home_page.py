import logging
import utilities.custom_logger as cl
from selenium.webdriver.common.by import By
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage


class HomePage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = 'Login'
    _practice = 'Practice'
    _header_logo = '.navbar-brand'  # css
    _headline = 'headline'
    _subtitle = 'subtitle'
    _featured_courses = "//h2[contains(text(),'Featured Courses')]"
    _primary_button = '.btn.btn-md.btn-primary'

    # Actions
    def verify_login_link_is_visible(self):
        return self.is_element_present(self._login_link, locator_type='link')

    def verify_practice_link_is_visible(self):
        return self.is_element_present(self._practice, locator_type='link')

    def verify_header_logo_is_visible(self):
        return self.is_element_present(self._header_logo, locator_type='css')

    def verify_headline_is_visible(self):
        return self.is_element_present(self._headline, locator_type='class')

    def verify_subtitle_is_visible(self):
        return self.is_element_present(self._subtitle, locator_type='class')

    def verify_featured_courses_is_visible(self):
        return self.is_element_present(self._featured_courses, locator_type='xpath')

    def verify_primary_button_is_visible(self):
        return self.is_element_present(self._primary_button, locator_type='css')
