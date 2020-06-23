import pytest
import unittest
import time
from pages.home.login_page import LoginPage
from selenium import webdriver


opt = webdriver.ChromeOptions()
opt.add_argument('user-data-dir=/Users/vrodikov/Library/Application Support/Google/Chrome/Default')
driver = webdriver.Chrome(options=opt, executable_path='/Users/vrodikov/PycharmProjects/letskodeit/resources/chromedriver')
driver.implicitly_wait(10)
base_url = 'https://letskodeit.teachable.com/'
driver.get(base_url)
time.sleep(5)
print("Running tests on Chrome")
lp = LoginPage(driver)
lp.login('test@email.com', 'abcabc')
result = lp.verify_login_successful()
assert result == True
time.sleep(5)
lp.logout()
driver.quit()