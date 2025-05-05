import unittest
from smartcart.cart import Cart


class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()

    def test_add_item(self):
        self.cart.add_item('apple', 1.99, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]['name'], 'apple')
        self.assertEqual(self.cart.items[0]['price'], 1.99)
        self.assertEqual(self.cart.items[0]['quantity'], 2)

    def test_remove_item(self):
        self.cart.add_item('banana', 0.99, 3)
        self.cart.remove_item('banana')
        self.assertEqual(len(self.cart.items), 0)

    def test_update_quantity(self):
        self.cart.add_item('orange', 0.5, 2)
        self.cart.update_quantity('orange', 5)
        self.assertEqual(self.cart.items[0]['quantity'], 5)

    def test_clear_cart(self):
        self.cart.add_item('milk', 2.5, 1)
        self.cart.clear_cart()
        self.assertEqual(len(self.cart.items), 0)

    def test_total_price(self):
        self.cart.add_item('bread', 3.0, 2)
        self.cart.add_item('butter', 2.0, 1)
        self.assertAlmostEqual(self.cart.total_price(), 8.0)

    def test_update_quantity_item_not_found(self):
        with self.assertRaises(ValueError):
            self.cart.update_quantity('ghost', 1)

    def test_remove_item_not_found(self):
        with self.assertRaises(ValueError):
            self.cart.remove_item('phantom')


if __name__ == '__main__':
    unittest.main()