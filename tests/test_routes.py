import pytest
from smartcart.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.app_context():      # ✅ required for current_app
        with app.test_client() as client:
            yield client

def test_add_item(client):
    response = client.post('/cart/add', json={
        "name": "banana",
        "price": 0.99,
        "quantity": 2
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Item added"

def test_view_cart(client):

    client.post('/cart/add', json={
        "name": "apple",
        "price": 1.00,
        "quantity": 3
    })
    
    response = client.get('/cart/view')
    assert response.status_code == 200
    data = response.get_json()
    
    assert "items" in data
    assert any(item["name"] == "apple" and item["quantity"] == 3 for item in data["items"])
    assert "subtotal" in data
    assert "tax" in data
    assert "shipping" in data
    assert "total" in data

def test_remove_item(client):
    client.post('/cart/add', json={"name": "milk", "price": 2.5, "quantity": 1})
    response = client.post('/cart/remove', json={"name": "milk"})
    assert response.status_code == 200
    assert response.get_json()["message"] == "Item removed"

def test_update_quantity(client):
    client.post('/cart/add', json={"name": "bread", "price": 1.5, "quantity": 1})
    response = client.post('/cart/update', json={"name": "bread", "quantity": 5})
    assert response.status_code == 200
    assert response.get_json()["message"] == "Quantity updated"

def test_apply_promo(client):
    client.post('/cart/add', json={"name": "eggs", "price": 5, "quantity": 1})
    response = client.post('/cart/apply-promo', json={"code": "10OFF"})
    data = response.get_json()
    assert response.status_code == 200
    assert "discounted_subtotal" in data
    assert "total" in data