import unittest



from smartcart.models import Cart


class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()

    def test_add_item(self):
        self.cart.add_item('apple', 1.99, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertIn('apple', self.cart.items)
        self.assertEqual(self.cart.items['apple'].price, 1.99)
        self.assertEqual(self.cart.items['apple'].quantity, 2)

    def test_remove_item(self):
        self.cart.add_item('banana', 0.99, 3)
        self.cart.remove_item('banana')
        self.assertNotIn('banana', self.cart.items)

    def test_update_quantity(self):
        self.cart.add_item('orange', 0.5, 2)
        self.cart.update_quantity('orange', 5)
        self.assertEqual(self.cart.items['orange'].quantity, 5)

    def test_clear_cart(self):
        self.cart.add_item('milk', 2.5, 1)
        self.cart.clear()
        self.assertEqual(len(self.cart.items), 0)

    def test_total_price(self):
        self.cart.add_item('bread', 3.0, 2)   # 6.0
        self.cart.add_item('butter', 2.0, 1)  # 2.0
        self.assertAlmostEqual(self.cart.get_total(), 8.0)

    def test_update_quantity_to_zero(self):
        self.cart.add_item('ghost', 5.0, 1)
        self.cart.update_quantity('ghost', 0)
        self.assertNotIn('ghost', self.cart.items)


if __name__ == '__main__':
    unittest.main()