def calculate_tax(subtotal, rate=0.085):
    return round(subtotal * rate, 2)

def calculate_shipping(subtotal):
    return 0 if subtotal >= 50 else 5.99

def apply_discount(subtotal, code):
    discounts = {'10OFF': 0.10, '20OFF': 0.20}
    if code in discounts:
        return round(subtotal * (1 - discounts[code]), 2)
    return subtotal