from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage

class TiebaHomePage(BasePage):
    '''贴吧首页的元素和操作'''
    def getLoginLink(self):
        return self.driver.find_element(By.LINK_TEXT, '登录')
