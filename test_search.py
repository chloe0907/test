import unittest

class Search:

    def search_func(self):
        print("search")


class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")
        cls.search = Search()

    def test_search1(self):
        print("test search1")
        self.assertIsNone(self.search.search_func())

    def test_search2(self):
        print("test search2")
        self.assertIsNone(self.search.search_func())

    def test_search3(self):
        print("test search3")
        self.assertIsNone(self.search.search_func())