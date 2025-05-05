import unittest
from smartcart.app import create_app
from smartcart.database import init_db


class TestDatabaseInit(unittest.TestCase):
    def test_init_db(self):
        app = create_app()
        with app.app_context():
            try:
                init_db()
            except Exception as e:
                self.fail(f"init_db() raised an exception: {e}")


if __name__ == '__main__':
    unittest.main()