import unittest
from PageObjects.BaiduHomePage import BaiduHomePage
from myunit.MyTest import MyTest
from myunit.Function import Function

class TestOpenBaiduTieba(MyTest):

    def test_openBaiduTieba(self):
        baiduHome = BaiduHomePage(self.driver)
        baiduHome.clickTiebaLink()
        current_title = self.driver.title
        self.assertEqual(current_title, '百度贴吧——全球最大的中文社区')
        screenShot = Function(self.driver)
        screenShot.save_screenshot(filename='open_BaiduTieba_success_')


if __name__ == '__main__':
    unittest.main()
