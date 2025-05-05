import unittest
from smartcart.app import create_app


class TestCartRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    def test_add_item(self):
        response = self.client.post('/cart/add', json={
            "name": "banana",
            "price": 0.99,
            "quantity": 2
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["message"], "Item added")

    def test_view_cart(self):
        self.client.post('/cart/add', json={
            "name": "apple",
            "price": 1.00,
            "quantity": 3
        })

        response = self.client.get('/cart/view')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("items", data)
        self.assertTrue(any(item["name"] == "apple" and item["quantity"] == 3 for item in data["items"]))
        self.assertIn("subtotal", data)
        self.assertIn("tax", data)
        self.assertIn("shipping", data)
        self.assertIn("total", data)

    def test_remove_item(self):
        self.client.post('/cart/add', json={"name": "milk", "price": 2.5, "quantity": 1})
        response = self.client.post('/cart/remove', json={"name": "milk"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["message"], "Item removed")

    def test_update_quantity(self):
        self.client.post('/cart/add', json={"name": "bread", "price": 1.5, "quantity": 1})
        response = self.client.post('/cart/update', json={"name": "bread", "quantity": 5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["message"], "Quantity updated")

    def test_apply_promo(self):
        self.client.post('/cart/add', json={"name": "eggs", "price": 5, "quantity": 1})
        response = self.client.post('/cart/apply-promo', json={"code": "10OFF"})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("discounted_subtotal", data)
        self.assertIn("total", data)


if __name__ == '__main__':
    unittest.main()