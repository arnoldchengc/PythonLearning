from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class WaitElement(object):
    '''等待元素的方法'''

    def __init__(self, driver):
        self.driver = driver

    def is_element_visibility(self, element, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of(element))
            print(str(element) + "is visibility")
            return True
        except:
            print(element + "is not visibility")
            return False


    def is_element_invisibility(self, element, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until_not(EC.visibility_of(element))
            return True
        except:
            print(element + "is still visibility")
            return False


    def is_element_clickable(self, locator, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            return True
        except:
            print(locator + "is not clickable at this time")
            return False

