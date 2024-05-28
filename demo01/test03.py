import unittest


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        print('tearDownClass')

    # def setUp(self) -> None:
    #     super().setUp()
    #     print('setup')

    def test1(self):
        print('test1')
        self.assertEqual(3, 1 + 2)

    def test2(self):
        print('test2')
        self.assertIn(2, [2, 3, 4])

    # def tearDown(self) -> None:
    #     super().tearDown()
    #     print('tearDown')
