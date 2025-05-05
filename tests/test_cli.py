import unittest
from unittest.mock import patch
from smartcart.cli import run_console
from io import StringIO


class TestCLI(unittest.TestCase):

    def run_with_inputs(self, inputs):
        with patch('builtins.input', side_effect=inputs), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            run_console()
            return mock_stdout.getvalue()

    def test_add_and_exit(self):
        output = self.run_with_inputs(["1", "banana", "0.99", "2", "7"])
        self.assertIn("Item added.", output)
        self.assertIn("Goodbye", output)

    def test_update_item(self):
        output = self.run_with_inputs(["1", "apple", "1.00", "2", "3", "apple", "5", "7"])
        self.assertIn("Quantity updated.", output)

    def test_apply_valid_promo(self):
        output = self.run_with_inputs(["1", "apple", "10", "1", "5", "10OFF", "7"])
        self.assertIn("Promo applied!", output)

    def test_clear_cart(self):
        output = self.run_with_inputs(["1", "apple", "1.00", "1", "6", "4", "7"])
        self.assertIn("Cart cleared.", output)
        self.assertIn("Cart is empty.", output)


if __name__ == '__main__':
    unittest.main()