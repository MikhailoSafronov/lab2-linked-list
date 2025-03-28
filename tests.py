import unittest
from linkedlist import ArrayList

class TestArrayList(unittest.TestCase):

    def test_length(self):
        arr = ArrayList()
        self.assertEqual(arr.length(), 0)
        arr.append('a')
        self.assertEqual(arr.length(), 1)

    def test_append_and_delete(self):
        arr = ArrayList()
        arr.append('a')
        arr.append('b')
        self.assertEqual(arr.delete(0), 'a')
        self.assertEqual(arr.delete(0), 'b')
        self.assertEqual(arr.length(), 0)

if __name__ == '__main__':
    unittest.main()
