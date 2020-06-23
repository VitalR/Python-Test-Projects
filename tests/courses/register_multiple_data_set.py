import pytest
import unittest
from ddt import ddt, data, unpack
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=1)
    @data(('Learn Python 3 from scratch', '4567 1234 7890 1010', '1023', '455', '452312'),
          ('Rest API Automation With Rest Assured', '4567 1234 7890 1010', '1023', '455', '452312'))
    @unpack
    def test_invalid_enrollment(self, course_name, cc_num, cc_exp, cc_vv, postal_code):
        self.courses.enter_course_name(course_name)
        self.courses.select_course_to_enroll(course_name)
        self.courses.enroll_course(num=cc_num, exp=cc_exp, cvv=cc_vv, postal_code=postal_code)
        result = self.courses.verify_enroll_failed()
        self.ts.mark_final('test_invalid_enrollment', result, 'Enrolment Failed Verification')
        # self.courses.logout()
        # self.driver.navigate().back()
        self.driver.find_element_by_xpath("//a[@class='navbar-brand header-logo']").click()
        # self.driver.find_element_by_link_text('All Courses')

        self.courses.logout()