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
            return True
        except:
            print(element + "is not visibility")
            return False

