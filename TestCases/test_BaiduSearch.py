import unittest
from PageObjects.BaiduHomePage import BaiduHomePage
from myunit.MyTest import MyTest
from myunit.Function import Function
from time import sleep

class TestBaiduSearch(MyTest):

    def test_BaiduSearch(self):
        baiduHome = BaiduHomePage(self.driver)
        baiduHome.inputSearchText(searchText="07297222")
        sleep(5)

if __name__ == "__main__":
    unittest.main()
