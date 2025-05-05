from flask import Flask
from smartcart.routes import cart_routes
from smartcart.database import init_db, close_db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['DATABASE'] = 'smartcart.db'

    with app.app_context():
        init_db()

    app.teardown_appcontext(close_db)
    app.register_blueprint(cart_routes, url_prefix='/cart')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)