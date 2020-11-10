from appium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

# for debug uncomment the next two lines:
import logging
logging.basicConfig(level=logging.DEBUG)

sauceParameters = {

    "platformName": "iOS",
    "platformVersion": "13.5.1",
    "browserName": "safari",
    # "deviceName": "iPhone_11_Pro_14_real_us",
    'testobject_api_key': 'D7A8AB865BEF475E88CB339D7E5B0024',
    "name": "Python test"
}


driver = webdriver.Remote(
    command_executor='http://us1.appium.testobject.com/wd/hub',
    # command_executor='https://eu1.appium.testobject.com/wd/hub',
    desired_capabilities=sauceParameters)

driver.get('https://www.google.com')

driver.quit()
