from time import time
from datetime import datetime
from PageObjects.BasePage import BasePage

class Function(object):

    def __init__(self, driver):
        self.driver = driver

    '''保存截图'''
    def save_screenshot(self, filename):
        now = datetime.now()
        currenttime = now.strftime("%Y%m%d%H%M%S")
        self.driver.get_screenshot_as_file('C:\\Users\\Arnold\\PycharmProjects\\PythonLearning\\Report\\image\\' + filename + currenttime + '.png')