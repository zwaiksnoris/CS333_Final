import unittest
from smartcart.promo import is_valid_promo, get_promo_effect


class TestPromo(unittest.TestCase):

    def test_valid_promo_codes(self):
        self.assertTrue(is_valid_promo('10OFF'))
        self.assertTrue(is_valid_promo('20OFF'))
        self.assertTrue(is_valid_promo('FREESHIP'))

    def test_invalid_promo_code(self):
        self.assertFalse(is_valid_promo('INVALID'))

    def test_get_promo_effect_valid(self):
        self.assertEqual(get_promo_effect('10OFF'), 0.10)
        self.assertEqual(get_promo_effect('FREESHIP'), 'free_shipping')

    def test_get_promo_effect_invalid(self):
        self.assertIsNone(get_promo_effect('INVALID'))


if __name__ == '__main__':
    unittest.main()