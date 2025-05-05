from smartcart.app import create_app
from smartcart.database import init_db

def test_init_db():
    app = create_app()
    with app.app_context():
        init_db()