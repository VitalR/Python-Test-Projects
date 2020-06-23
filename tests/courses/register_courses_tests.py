import pytest
import unittest
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=1)
    def test_invalid_enrollment(self):
        self.courses.enter_course_name('Python 3')
        # self.courses.click_on_search_button()
        self.courses.select_course_to_enroll('Learn Python 3 from scratch')
        self.courses.enroll_course(num='4567 1234 7890 1010', exp='1023', cvv='455', postal_code='452312')
        result = self.courses.verify_enroll_failed()
        self.ts.mark_final('test_invalid_enrollment', result, 'Enrolment Failed Verification')
        self.courses.logout()
