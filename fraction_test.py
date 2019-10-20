import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_init_with_int_type(self):
        self.assertIsInstance(Fraction(0), Fraction)
        self.assertIsInstance(Fraction(1), Fraction)
        self.assertIsInstance(Fraction(3*3, 2*8), Fraction)
        self.assertIsInstance(Fraction(5**3), Fraction)

    def test_init_with_not_int_type(self):
        with self.assertRaises(TypeError):
            Fraction("string")

        with self.assertRaises(TypeError):
            Fraction(None, None)

        with self.assertRaises(TypeError):
            Fraction(True, True)

    def test_str(self):
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())

        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())

        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())

        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())

        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())

        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())

        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())

        f = Fraction(99)
        self.assertEqual("99", f.__str__())

        f = Fraction(0, 0)
        self.assertEqual("nan", f.__str__())

    def test_repr(self):
        f = Fraction(-80, 20)
        self.assertEqual("Fraction(-4, 1)", f.__repr__())

        f = Fraction(3, -1)
        self.assertEqual("Fraction(3, -1)", f.__repr__())

        f = Fraction(36, -60)
        self.assertEqual("Fraction(3, -5)", f.__repr__())

        f = Fraction(0, 5)
        self.assertEqual("Fraction(0, 1)", f.__repr__())

        f = Fraction(60, 90)
        self.assertEqual("Fraction(2, 3)", f.__repr__())

        f = Fraction(1500, 60)
        self.assertEqual("Fraction(25, 1)", f.__repr__())

        f = Fraction(1500, 90)
        self.assertEqual("Fraction(50, 3)", f.__repr__())

        f = Fraction(99)
        self.assertEqual("Fraction(99, 1)", f.__repr__())

        f = Fraction(99, 0)
        self.assertEqual("Fraction(99, 0)", f.__repr__())

    def test_eq(self):
        neg_one_over_seven = Fraction(-1, 7)
        neg_one_over_neg_two = Fraction(-1, -2)
        neg_fourty_over_neg_eighteen = Fraction(-40, -80)
        one_over_two = Fraction(1, 2)
        one_over_neg_seven = Fraction(1, -7)
        ten_k_over_twenty_k_and_one = Fraction(10000, 20001)
        zero_over_nine = Fraction(0, 9)
        zero_over_zero = Fraction(0, 0)

        self.assertEqual(neg_fourty_over_neg_eighteen, neg_one_over_neg_two)
        self.assertEqual(one_over_two, neg_fourty_over_neg_eighteen)
        self.assertEqual(one_over_neg_seven, neg_one_over_seven)
        self.assertEqual(one_over_two, neg_one_over_neg_two)

        self.assertNotEqual(one_over_two, ten_k_over_twenty_k_and_one)
        self.assertNotEqual(ten_k_over_twenty_k_and_one, one_over_neg_seven)
        self.assertNotEqual(zero_over_nine, one_over_neg_seven)
        self.assertNotEqual(zero_over_nine, one_over_neg_seven)
        self.assertNotEqual(zero_over_zero, zero_over_zero)

    def test_add(self):
        self.assertEqual(Fraction(0), Fraction(25, 100) + Fraction(-1, 4))
        self.assertEqual(Fraction(0), Fraction(0, 100) + Fraction(0, 4))
        self.assertEqual(Fraction(1, 2), Fraction(25, 100) + Fraction(1, 4))
        self.assertEqual(Fraction(-3, 2), Fraction(-2, 1) + Fraction(1, 2))
        self.assertEqual(Fraction(3, 4), Fraction(1, 12) + Fraction(2, 3))

        self.assertTrue(math.isnan(Fraction(1, 12) + Fraction(2, 0)))

    def test_sub(self):
        self.assertEqual(Fraction(0), Fraction(25, 100) - Fraction(1, 4))
        self.assertEqual(Fraction(0), Fraction(0, 100) - Fraction(0, 4))
        self.assertEqual(Fraction(-5, 2), Fraction(-2, 1) - Fraction(1, 2))
        self.assertEqual(Fraction(1, 2), Fraction(25, 100) - Fraction(-1, 4))
        self.assertEqual(Fraction(-7, 12), Fraction(1, 12) - Fraction(2, 3))

        self.assertTrue(math.isnan(Fraction(0, 0) - Fraction(2, 3)))

    def test_mul(self):
        self.assertEqual(Fraction(0), Fraction(0) * Fraction(0))
        self.assertEqual(Fraction(0), Fraction(2) * Fraction(3) * Fraction(0))
        self.assertEqual(Fraction(1), Fraction(1, 3) * Fraction(3))
        self.assertEqual(Fraction(2, 27), Fraction(1, 3) * Fraction(2, 9))
        self.assertEqual(Fraction(6), Fraction(2) * Fraction(3))

        self.assertTrue(math.isnan(Fraction(0, 0) * Fraction(2, 3)))

    def test_div(self):
        self.assertEqual(Fraction(2), Fraction(2) / Fraction(1))
        self.assertEqual(Fraction(2, 3), Fraction(2) / Fraction(3))
        self.assertEqual(Fraction(1, 9), Fraction(1, 3) / Fraction(3))
        self.assertEqual(Fraction(63, 24), Fraction(7, 3) / Fraction(8, 9))
        self.assertEqual(Fraction(2, 3), Fraction(2) / Fraction(3))

        self.assertTrue(math.isnan(Fraction(0, 0) / Fraction(2, 3)))

    def test_gt(self):
        self.assertGreater(Fraction(0, 2), Fraction(1, -4))
        self.assertGreater(Fraction(1, 2), Fraction(1, 4))
        self.assertGreater(Fraction(9, 27), Fraction(25, 100))

        self.assertFalse(Fraction(0) > Fraction(0))
        self.assertFalse(Fraction(1, 100) > Fraction(1, 10))
        self.assertFalse(Fraction(-10, 2) > Fraction(-1, 4))
        self.assertFalse(Fraction(1, 0) > Fraction(0, 0))

    def test_lt(self):
        self.assertLess(Fraction(-10, 2), Fraction(-1, 4))
        self.assertLess(Fraction(-1, 2), Fraction(1, 2))
        self.assertLess(Fraction(1, 100), Fraction(1, 10))

        self.assertFalse(Fraction(0, 2) < Fraction(1, -4))
        self.assertFalse(Fraction(1, 2) < Fraction(1, 4))
        self.assertFalse(Fraction(9, 27) < Fraction(25, 100))
        self.assertFalse(Fraction(-9, 0) < Fraction(0, 0))

    def test_neg(self):
        self.assertEqual(Fraction(-1, 2), -Fraction(1, 2))
        self.assertEqual(Fraction(-1), -Fraction(1))
        self.assertEqual(Fraction(-1, 2), -Fraction(1, 2))
        self.assertEqual(Fraction(-1, -2), -Fraction(-1, 2))
        self.assertEqual(Fraction(1, 2), -Fraction(-1, 2))

        self.assertTrue(math.isnan(-Fraction(-1, 0)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
