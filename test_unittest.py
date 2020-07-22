import unittest

class TestDemo(unittest.TestCase):

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("tear down")

    @classmethod
    def setUpClass(cls) -> None:
        print("class setup")

    @classmethod
    def tearDownClass(cls) -> None:
        print("class tear down")

    def test_upper(self):
        print("test upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("test isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("test_split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
