import pytest
import unittest
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalid_login_01(self):
        self.lp.logout()
        self.lp.login('', '')
        result = self.lp.verify_login_failed()
        assert result == False

    @pytest.mark.run(order=2)
    def test_invalid_login_02(self):
        self.lp.login('test@email.com', 'invalidpassw')
        result = self.lp.verify_login_failed()
        assert result == False

    @pytest.mark.run(order=3)
    def test_valid_login(self):
        self.lp.login('test@email.com', 'abcabc')
        result1 = self.lp.verify_login_title()
        self.ts.mark(result1, 'Title Verification')
        # assert result1 == True
        result2 = self.lp.verify_login_successful()
        self.ts.mark_final('test_valid_login', result2, 'Login was successful')
        # assert result2 == True
        self.lp.logout()

        # self.driver.quit()