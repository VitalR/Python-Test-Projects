"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import time
import traceback
from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        opt = webdriver.ChromeOptions()
        opt.add_argument('user-data-dir=/Users/Library/Application Support/Google/Chrome/Default')
        # driver = webdriver.Chrome(options=opt, executable_path='resources/chromedriver')
        baseURL = "https://letskodeit.teachable.com/"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path='resources/geckodriver')
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome(options=opt, executable_path='resources/chromedriver')
            # driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome(options=opt, executable_path='resources/chromedriver')
            # driver = webdriver.Chrome()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(10)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        try:
            item = driver.find_element_by_class_name('gravatar').is_displayed()
            if item:
                driver.find_element_by_class_name('gravatar').click()
                driver.find_element_by_class_name('user-signout').click()
        except:
            print('The user is login it')
        # time.sleep(2)
        return driver
