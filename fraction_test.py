import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_init(self):
        with self.assertRaises(TypeError):
            Fraction("string")
        with self.assertRaises(TypeError):
            Fraction(None, None)
        with self.assertRaises(TypeError):
            Fraction(True, True)
        with self.assertRaises(ValueError):
            Fraction(1, 0)
        with self.assertRaises(ValueError):
            Fraction(-1, 0)

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        f = Fraction(99)
        self.assertEqual("99", f.__str__())

    def test_eq(self):
        f = Fraction(1, 2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001)
        i = Fraction(0, 9)
        j = Fraction(1, -7)
        k = Fraction(-1, 7)
        l = Fraction(-1, -2)

        self.assertTrue(f == g)
        self.assertFalse(f == h)
        self.assertFalse(i == j)
        self.assertFalse(i == f)
        self.assertTrue(j == k)
        self.assertTrue(f == l)
        self.assertTrue(g == l)

    def test_add(self):
        self.assertEqual(Fraction(3, 4), Fraction(1, 12) + Fraction(2, 3))
        self.assertEqual(Fraction(1, 2), Fraction(25, 100) + Fraction(1, 4))
        self.assertEqual(Fraction(0), Fraction(25, 100) + Fraction(-1, 4))
        self.assertEqual(Fraction(0), Fraction(0, 100) + Fraction(0, 4))
        self.assertEqual(Fraction(-3, 2), Fraction(-2, 1) + Fraction(1, 2))

    def test_sub(self):
        self.assertEqual(Fraction(-7, 12), Fraction(1, 12) - Fraction(2, 3))
        self.assertEqual(Fraction(0), Fraction(25, 100) - Fraction(1, 4))
        self.assertEqual(Fraction(1, 2), Fraction(25, 100) - Fraction(-1, 4))
        self.assertEqual(Fraction(0), Fraction(0, 100) - Fraction(0, 4))
        self.assertEqual(Fraction(-5, 2), Fraction(-2, 1) - Fraction(1, 2))

    def test_mul(self):
        self.assertEqual(Fraction(1), Fraction(1, 3) * Fraction(3))
        self.assertEqual(Fraction(6), Fraction(2) * Fraction(3))
        self.assertEqual(Fraction(2, 27), Fraction(1, 3) * Fraction(2, 9))
        self.assertEqual(Fraction(0), Fraction(0) * Fraction(0))
        self.assertEqual(Fraction(0), Fraction(2) * Fraction(3) * Fraction(0))

    def test_gt(self):
        self.assertTrue(Fraction(1, 2) > Fraction(1, 4))
        self.assertTrue(Fraction(0, 2) > Fraction(1, -4))
        self.assertTrue(Fraction(9, 27) > Fraction(25, 100))
        self.assertFalse(Fraction(-10, 2) > Fraction(-1, 4))
        self.assertFalse(Fraction(0) > Fraction(0))
        self.assertFalse(Fraction(1, 100) > Fraction(1, 10))
