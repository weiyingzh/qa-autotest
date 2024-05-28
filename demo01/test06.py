import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from lib import HTMLTestRunner

class TestCase1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')

    def testsearch(self):
        input = self.driver.find_element_by_id('kw')
        input.send_keys('玩转pycharm 郭宏志')

        btn = self.driver.find_element_by_id('su')
        ActionChains(self.driver).click(btn).perform()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(unittest.makeSuite(TestCase1))
    fp = open(r".\result.html","wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="百度搜索测试报告", description="用例执行情况")
    runner.run(testunit)
    fp.close()
