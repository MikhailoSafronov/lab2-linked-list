import unittest
from linkedlist import CircularLinkedList

class TestCircularLinkedList(unittest.TestCase):

    def test_length(self):
        cll = CircularLinkedList()
        self.assertEqual(cll.length(), 0)
        cll.append('a')
        self.assertEqual(cll.length(), 1)

    def test_append_and_delete(self):
        cll = CircularLinkedList()
        cll.append('a')
        cll.append('b')
        self.assertEqual(cll.delete(0), 'a')
        self.assertEqual(cll.delete(0), 'b')
        self.assertEqual(cll.length(), 0)

if __name__ == '__main__':
    unittest.main()
