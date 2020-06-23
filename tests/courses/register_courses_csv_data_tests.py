import pytest
import unittest
from ddt import ddt, data, unpack
from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.read_data import get_csv_data
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self) -> None:
        self.nav.navigate_to_all_courses()

    @pytest.mark.run(order=1)
    @data(*get_csv_data('testdata/testdata.csv'))
    @unpack
    def test_invalid_enrollment(self, course_name, cc_num, cc_exp, cc_vv, postal_code):
        self.courses.enter_course_name(course_name)
        self.courses.select_course_to_enroll(course_name)
        self.courses.enroll_course(num=cc_num, exp=cc_exp, cvv=cc_vv, postal_code=postal_code)
        result = self.courses.verify_enroll_failed()
        self.ts.mark_final('test_invalid_enrollment', result, 'Enrolment Failed Verification')
        self.driver.find_element_by_xpath("//a[@class='navbar-brand header-logo']").click()
