import unittest, time
from HTMLTestRunner import HTMLTestRunner

test_dir = './TestCases'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    print(now)
    filename = './Report/' + now + '_result.html'
    fp = open(filename, 'wb')

    runner = HTMLTestRunner(stream=fp, title='My Test Result', description='Test Description')
    runner.run(discover)
    fp.close()

