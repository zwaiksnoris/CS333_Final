from smartcart.models import Cart

def test_add_item():
    cart = Cart()
    cart.add_item("apple", 1.99, 1)
    assert "apple" in cart.items
    assert cart.items["apple"].quantity == 1
    assert cart.items["apple"].price == 1.99

def test_update_quantity():
    cart = Cart()
    cart.add_item("apple", 1.99, 1)
    cart.update_quantity("apple", 3)
    assert cart.items["apple"].quantity == 3

def test_remove_item():
    cart = Cart()
    cart.add_item("apple", 1.99, 1)
    cart.remove_item("apple")
    assert "apple" not in cart.items

def test_get_total():
    cart = Cart()
    cart.add_item("apple", 1.00, 2)
    cart.add_item("banana", 2.00, 1)
    total = cart.get_total()
    assert total == 4.00

def test_clear():
    cart = Cart()
    cart.add_item("apple", 1.00, 1)
    cart.clear()
    assert len(cart.items) == 0