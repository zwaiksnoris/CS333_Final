from smartcart.models import Cart
from smartcart.price_calc import calculate_tax, calculate_shipping, apply_discount
from smartcart.promo import is_valid_promo

def display_cart(cart):
    if not cart.items:
        print("\nCart is empty.\n")
        return

    print("\nCart Contents:")
    for item in cart.items.values():
        print(f"- {item.name} | ${item.price:.2f} x {item.quantity}")
    subtotal = cart.get_total()
    tax = calculate_tax(subtotal)
    shipping = calculate_shipping(subtotal)
    total = round(subtotal + tax + shipping, 2)
    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Shipping: ${shipping:.2f}")
    print(f"Total: ${total:.2f}\n")

def run_console():
    cart = Cart()
    print("Welcome to SmartCart Console Edition 🛒")

    while True:
        print("""
Options:
1. Add item
2. Remove item
3. Update quantity
4. View cart
5. Apply promo code
6. Clear cart
7. Exit
""")
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            name = input("Item name: ").strip()
            try:
                price = float(input("Item price: ").strip())
                quantity = int(input("Quantity: ").strip())
            except ValueError:
                print("Invalid price or quantity.")
                continue
            cart.add_item(name, price, quantity)
            print("Item added.")

        elif choice == "2":
            name = input("Item name to remove: ").strip()
            cart.remove_item(name)
            print("Item removed.")

        elif choice == "3":
            name = input("Item name to update: ").strip()
            try:
                quantity = int(input("New quantity: ").strip())
            except ValueError:
                print("Invalid quantity.")
                continue
            cart.update_quantity(name, quantity)
            print("Quantity updated.")

        elif choice == "4":
            display_cart(cart)

        elif choice == "5":
            code = input("Enter promo code: ").strip()
            if not is_valid_promo(code):
                print("Invalid promo code.")
                continue
            subtotal = cart.get_total()
            discounted = apply_discount(subtotal, code)
            tax = calculate_tax(discounted)
            shipping = 0 if code == "FREESHIP" else calculate_shipping(discounted)
            total = round(discounted + tax + shipping, 2)
            print(f"\nPromo applied! New total: ${total:.2f}\n")

        elif choice == "6":
            cart.clear()
            print("Cart cleared.")

        elif choice == "7":
            print("Thanks for using SmartCart. Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_console()