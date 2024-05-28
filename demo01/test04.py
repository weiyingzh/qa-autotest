import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

class MyTestCase(unittest.TestCase):

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