import pytest
import unittest
import time
from selenium import webdriver
from pages.home.login_page import LoginPage


class LoginTests(unittest.TestCase):
    # opt = webdriver.ChromeOptions()
    # opt.add_argument('user-data-dir=/Users/vrodikov/Library/Application Support/Google/Chrome/Default')
    # driver = webdriver.Chrome(options=opt, executable_path='resources/chromedriver')
    # driver.implicitly_wait(10)
    #
    # base_url = 'https://letskodeit.teachable.com/'
    # # driver = webdriver.Chrome(executable_path='resources/chromedriver')
    #
    #
    # lp = LoginPage(driver)
    # time.sleep(5)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument('user-data-dir=/Users/vrodikov/Library/Application Support/Google/Chrome/Default')
        driver = webdriver.Chrome(options=opt, executable_path='resources/chromedriver')
        driver.implicitly_wait(10)
        base_url = 'https://letskodeit.teachable.com/'
        driver.get(base_url)
        time.sleep(5)

        lp = LoginPage(driver)
        lp.login('test@email.com', 'abcabc')

        result = lp.verify_login_successful()
        assert result == True

        driver.quit()

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument('user-data-dir=/Users/vrodikov/Library/Application Support/Google/Chrome/Default')
        driver = webdriver.Chrome(options=opt, executable_path='resources/chromedriver')
        driver.implicitly_wait(10)
        base_url = 'https://letskodeit.teachable.com/'
        driver.get(base_url)
        time.sleep(5)

        lp = LoginPage(driver)
        lp.login('', '')
        result = lp.verify_login_failed()
        assert result == False

        driver.quit()

# ff = LoginTests()
# ff.test_valid_login()
