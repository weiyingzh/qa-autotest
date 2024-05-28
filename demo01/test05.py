import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains


class TestCase1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')

    def test1(self):
        input = self.driver.find_element_by_id('kw')
        input.send_keys('玩转pycharm 郭宏志')

        btn = self.driver.find_element_by_id('su')

        ActionChains(self.driver).click(btn).perform()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()


class TestCase2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.jd.com')

    def test2(self):
        input = self.driver.find_element_by_id('key')
        input.send_keys('郭宏志')

        btn = self.driver.find_element_by_class_name('cw-icon')

        ActionChains(self.driver).click(btn).perform()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()


if __name__ == '__main__':
    testcase1 = unittest.TestLoader.loadTestsFromTestCase(TestCase1)
    testcase2 = unittest.TestLoader.loadTestsFromTestCase(TestCase2)

    unittest.TestSuite.run([testcase1, testcase2])
