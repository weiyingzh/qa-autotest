import csv
import unittest

from ddt import ddt, data, unpack
from selenium import webdriver
from time import sleep

def get_csv_data(csv_path):
    rows = []
    csv_data = open(str(csv_path), "r")
    content = csv.reader(csv_data)

    for row in content:
        rows.append(row)
        print(row)
    return rows

@ddt
class TestCast1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)

    @data(*get_csv_data('test.csv'))
    @unpack
    def test_search(self, target_url, elem_id, search_value):
        driver = self.driver
        driver.get(target_url)

        input_elem = driver.find_element_by_id(elem_id)
        input_elem.clear()
        input_elem.send_keys(search_value)
        input_elem.submit()

        sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        cls.driver.quit()

if __name__ == '__main__':
    testcast = unittest.TestLoader().loadTestsFromTestCase(TestCast1)
    test_suite = unittest.TestSuite([testcast])
    unittest.TextTestRunner(verbosity=2).run(test_suite)