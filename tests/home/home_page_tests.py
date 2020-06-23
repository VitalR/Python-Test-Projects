import pytest
import unittest
from pages.home.home_page import HomePage
from utilities.teststatus import TestStatus
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class HomePageTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)
        self.lp.logout()

    @pytest.mark.run(order=1)
    def test_home_page_elements_01(self):
        result = self.hp.verify_login_link_is_visible()
        assert result == True

    @pytest.mark.run(order=2)
    def test_home_page_elements_02(self):
        result = self.hp.verify_practice_link_is_visible()
        assert result == True

    @pytest.mark.run(order=3)
    def test_home_page_elements_03(self):
        result = self.hp.verify_header_logo_is_visible()
        assert result == True

    @pytest.mark.run(order=4)
    def test_home_page_elements_04(self):
        result = self.hp.verify_headline_is_visible()
        assert result == True

    @pytest.mark.run(order=5)
    def test_home_page_elements_05(self):
        result = self.hp.verify_subtitle_is_visible()
        assert result == True

    @pytest.mark.run(order=6)
    def test_home_page_elements_06(self):
        result = self.hp.verify_featured_courses_is_visible()
        assert result == True

    @pytest.mark.run(order=7)
    def test_home_page_elements_07(self):
        result = self.hp.verify_primary_button_is_visible()
        assert result == True
