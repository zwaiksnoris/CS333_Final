VALID_PROMOS = {
    '10OFF': 0.10,
    '20OFF': 0.20,
    'FREESHIP': 'free_shipping'
}

def is_valid_promo(code):
    return code in VALID_PROMOS

def get_promo_effect(code):
    return VALID_PROMOS.get(code)