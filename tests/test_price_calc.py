from smartcart.price_calc import calculate_tax, calculate_shipping, apply_discount

def test_calculate_tax():
    assert calculate_tax(100.0) == 8.5
    assert calculate_tax(0) == 0.0

def test_calculate_shipping_under_threshold():
    assert calculate_shipping(49.99) == 5.99

def test_calculate_shipping_free():
    assert calculate_shipping(50.00) == 0.0
    assert calculate_shipping(100.00) == 0.0

def test_apply_discount_valid():
    assert apply_discount(100.0, '10OFF') == 90.0
    assert apply_discount(100.0, '20OFF') == 80.0

def test_apply_discount_invalid():
    assert apply_discount(100.0, 'INVALID') == 100.0