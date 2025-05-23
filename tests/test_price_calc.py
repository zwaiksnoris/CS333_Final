import unittest
from smartcart.price_calc import calculate_tax, calculate_shipping, apply_discount


class TestPriceCalc(unittest.TestCase):

    def test_calculate_tax(self):
        self.assertEqual(calculate_tax(100.0), 8.5)
        self.assertEqual(calculate_tax(0), 0.0)

    def test_calculate_shipping_under_threshold(self):
        self.assertEqual(calculate_shipping(49.99), 5.99)

    def test_calculate_shipping_free(self):
        self.assertEqual(calculate_shipping(50.00), 0.0)
        self.assertEqual(calculate_shipping(100.00), 0.0)

    def test_apply_discount_valid(self):
        self.assertEqual(apply_discount(100.0, '10OFF'), 90.0)
        self.assertEqual(apply_discount(100.0, '20OFF'), 80.0)

    def test_apply_discount_invalid(self):
        self.assertEqual(apply_discount(100.0, 'INVALID'), 100.0)


if __name__ == '__main__':
    unittest.main()