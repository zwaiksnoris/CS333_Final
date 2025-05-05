from smartcart.promo import is_valid_promo, get_promo_effect

def test_valid_promo_codes():
    assert is_valid_promo('10OFF')
    assert is_valid_promo('20OFF')
    assert is_valid_promo('FREESHIP')

def test_invalid_promo_code():
    assert not is_valid_promo('INVALID')

def test_get_promo_effect_valid():
    assert get_promo_effect('10OFF') == 0.10
    assert get_promo_effect('FREESHIP') == 'free_shipping'

def test_get_promo_effect_invalid():
    assert get_promo_effect('INVALID') is None