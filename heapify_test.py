import unittest

from heapify import heapify

class heapify_test(unittest.TestCase):

    def test_empty_array(self):
        self.assertListEqual([], heapify([]))

    def test_array_of_one(self):
        self.assertListEqual([5], heapify([5]))

    def test_is_integer_array(self):
        self.assertRaises(TypeError, ["g","a","m","e"])

    def test_example1(self):
        self.assertListEqual([84, 22, 19, 10, 3, 17, 6, 5, 9], 
        heapify([5, 3, 17, 10, 84, 19, 6, 22, 9]))

if __name__ == '__main__':
    unittest.main()
