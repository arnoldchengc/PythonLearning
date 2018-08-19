from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage
from myunit.WaitElement import WaitElement

class BaiduHomePage(BasePage):
    '''百度首页的元素和操作'''

    def getTiebaLink(self):
        '''贴吧链接'''
        return self.driver.find_element(By.LINK_TEXT, '贴吧')

    def clickTiebaLink(self, timeout=30):
        waitElement = WaitElement(self.driver)
        waitElement.is_element_visibility(element=self.getTiebaLink())
        self.getTiebaLink().click()

