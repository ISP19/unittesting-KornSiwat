import unittest
from listutil import unique


class UniqueTest(unittest.TestCase):
    """Test the methods of the Unique method. """

    def test_empty_list(self):
        self.assertEqual([], unique([]))

    def test_one_element(self):
        self.assertEqual(["isp"], unique(["isp"]))
        self.assertEqual([[]], unique([[]]))

    def test_one_element_many_times(self):
        self.assertEqual(["isp"], unique(["isp", "isp", "isp", "isp", "isp"]))
        self.assertEqual([[1]], unique([[1], [1], [1]]))
        self.assertEqual([2**16, 2**9], unique([2**16, 2**9, 2**9, 2**16]))

    def test_two_element(self):
        self.assertEqual(["isp", "ske"], unique(["isp", "ske"]))
        self.assertEqual([[1], [2]], unique([[1], [2]]))

    def test_two_element_many_times(self):
        self.assertEqual([1, 2], unique([1, 1, 1, 2, 2, 1, 1, 2, 1, 1]))
        self.assertEqual([1, True], unique([1, True]))
        self.assertEqual([1, "1"], unique([1, "1"]))
        self.assertEqual([True, "True"], unique([True, "True"]))
        self.assertEqual([1,[[1]]], unique([1, [[1]]]))

    def test_wrong_type_input(self):
        with self.assertRaises(TypeError):
            unique(True)
        with self.assertRaises(TypeError):
            unique(0)
        with self.assertRaises(TypeError):
            unique(3.145723929)
        with self.assertRaises(TypeError):
            unique("ISP is challenging")