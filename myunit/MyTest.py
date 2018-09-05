from selenium import webdriver
import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome()
        self.driver = driver
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(15)


    def tearDown(self):
        self.driver.quit()

