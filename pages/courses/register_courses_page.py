import time
import logging
import utilities.custom_logger as cl
from base.basepage import BasePage


class RegisterCoursesPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "search-courses"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _search_button = "//button[@id='search-course-button']"
    _all_courses = "course-listing-title"
    _enroll_button = "enroll-button-top"
    _cc_num = "input[name='cardnumber']"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    _postal_code = "postal"
    _submit_enroll = "//div[@id='new_card']//button[contains(text(),'Enroll in Course')]"
    _agreed_checkbox = "agreed_to_terms_checkbox"
    _enroll_error_message = "//div[@id='new_card']//div[contains(text(),'The card number is not a valid credit card number.')]"
    _logout_link = "//div[@id='react-checkout']/div/div/div[2]//div[@class='_3x1ps dsp-flex-xs flex-align-items-baseline-xs']/button[@type='button']"

    # Actions
    def enter_course_name(self, course_name):
        self.send_data(course_name, locator=self._search_box)
        self.element_click(locator=self._search_button, locator_type="xpath")

    def select_course_to_enroll(self, full_course_name):
        self.element_click(locator=self._course.format(full_course_name), locator_type="xpath")

    def click_on_enroll_button(self):
        self.element_click(locator=self._enroll_button)

    def enter_card_num(self, num):
        # This frame takes at least 6 seconds to show
        time.sleep(3)
        # self.switch_to_frame(name="__privateStripeFrame16")
        self.switch_frame_by_index(self._cc_num, locator_type="css")
        self.send_data_when_ready(num, locator=self._cc_num, locator_type="css")
        # self.send_data(num, locator=self._cc_num, locator_type="css")
        self.switch_to_default_content()

    def enter_card_exp(self, exp):
        # self.switch_to_frame(name="__privateStripeFrame17")
        self.switch_frame_by_index(self._cc_exp, locator_type="name")
        self.send_data(exp, locator=self._cc_exp, locator_type="name")
        self.switch_to_default_content()

    def enter_card_cvv(self, cvv):
        # self.switch_to_frame(name="__privateStripeFrame18")
        self.switch_frame_by_index(self._cc_cvv, locator_type="name")
        self.send_data(cvv, locator=self._cc_cvv, locator_type="name")
        self.switch_to_default_content()

    def enter_postal_code(self, postal_code):
        # self.switch_to_frame(name="__privateStripeFrame19")
        self.switch_frame_by_index(self._postal_code, locator_type="name")
        self.send_data(postal_code, locator=self._postal_code, locator_type="name")
        self.switch_to_default_content()

    def click_enroll_submit_button(self):
        self.element_click(self._submit_enroll, locator_type="xpath")

    def enter_credit_card_information(self, num, exp, cvv, postal_code):
        self.enter_card_num(num)
        self.enter_card_exp(exp)
        self.enter_card_cvv(cvv)
        self.enter_postal_code(postal_code)
        # Hint: Call all three methods to enter card details

    def enroll_course(self, num="", exp="", cvv="", postal_code=""):
        self.click_on_enroll_button()
        self.webscroll(direction='down')
        self.enter_credit_card_information(num, exp, cvv, postal_code)
        self.element_click(self._agreed_checkbox)
        self.click_enroll_submit_button()
        # Hint:
        # • Click on the enroll button
        # • Scroll down
        # • Enter credit card information
        # • Click Enroll in course button

    def logout(self):
        self.element_click(self._logout_link, locator_type='xpath')

    def verify_enroll_failed(self):
        result = self.is_enabled(locator=self._submit_enroll, locator_type="xpath", info="Enroll Button")
        return not result
        # Verify the element for error message is displayed, not just present.
        # You need to verify if it is displayed
        # Hint: The element is not instantly displayed, it take some time to display
        # You need to wait for it to display
