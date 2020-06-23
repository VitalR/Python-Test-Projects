import time
import logging
import utilities.custom_logger as cl
from selenium.webdriver.common.by import By
from base.basepage import BasePage


class NavigationPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = 'My Courses'  # link_text
    _all_courses = 'All Courses'
    _practice = 'Practice'
    _user_icon = 'gravatar'  # class

    # Actions
    def navigate_to_my_courses(self):
        self.element_click(self._my_courses, locator_type='link')

    def navigate_to_all_courses(self):
        self.element_click(self._all_courses, locator_type='link')

    def navigate_to_practice(self):
        self.element_click(self._practice, locator_type='link')

    def navigate_to_user_icon(self):
        self.element_click(self._user_icon, locator_type='class')

