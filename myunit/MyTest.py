from selenium import webdriver
import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome()
        self.driver = driver
        self.driver.get("https://www.baidu.com")

    def tearDown(self):
        self.driver.quit()

