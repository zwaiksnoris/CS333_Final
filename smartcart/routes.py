from flask import Blueprint, request, jsonify
from smartcart.models import Cart
from smartcart.price_calc import calculate_tax, calculate_shipping, apply_discount
from smartcart.promo import is_valid_promo

cart_routes = Blueprint("cart_routes", __name__)
cart = Cart()

@cart_routes.route("/add", methods=["POST"])
def add_item():
    data = request.get_json()
    if not all(k in data for k in ("name", "price")):
        return jsonify({"error": "Missing name or price"}), 400

    cart.add_item(
        name=data["name"],
        price=float(data["price"]),
        quantity=int(data.get("quantity", 1))
    )
    return jsonify({"message": "Item added"}), 200

@cart_routes.route("/remove", methods=["POST"])
def remove_item():
    data = request.get_json()
    if "name" not in data:
        return jsonify({"error": "Missing item name"}), 400

    cart.remove_item(data["name"])
    return jsonify({"message": "Item removed"}), 200

@cart_routes.route("/update", methods=["POST"])
def update_quantity():
    data = request.get_json()
    if "name" not in data or "quantity" not in data:
        return jsonify({"error": "Missing name or quantity"}), 400

    cart.update_quantity(data["name"], int(data["quantity"]))
    return jsonify({"message": "Quantity updated"}), 200

@cart_routes.route("/clear", methods=["POST"])
def clear_cart():
    cart.clear()
    return jsonify({"message": "Cart cleared"}), 200

@cart_routes.route("/view", methods=["GET"])
def view_cart():
    subtotal = cart.get_total()
    tax = calculate_tax(subtotal)
    shipping = calculate_shipping(subtotal)
    total = round(subtotal + tax + shipping, 2)

    items = [
        {"name": item.name, "price": item.price, "quantity": item.quantity}
        for item in cart.items.values()
    ]
    return jsonify({
        "items": items,
        "subtotal": round(subtotal, 2),
        "tax": round(tax, 2),
        "shipping": round(shipping, 2),
        "total": total
    }), 200

@cart_routes.route("/apply-promo", methods=["POST"])
def apply_promo():
    data = request.get_json()
    code = data.get("code")
    if not code or not is_valid_promo(code):
        return jsonify({"error": "Invalid promo code"}), 400

    subtotal = cart.get_total()
    discounted = apply_discount(subtotal, code)
    tax = calculate_tax(discounted)
    shipping = 0 if code.upper() == "FREESHIP" else calculate_shipping(discounted)
    total = round(discounted + tax + shipping, 2)

    return jsonify({
        "subtotal": round(subtotal, 2),
        "discounted_subtotal": round(discounted, 2),
        "tax": round(tax, 2),
        "shipping": round(shipping, 2),
        "total": total
    }), 200