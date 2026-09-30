def calculate_tax(amount):
    """Returns a flat 10% tax on the amount."""
    return amount * 0.10

def calculate_total(cart_items):
    """Calculates the subtotal and adds tax."""
    subtotal = sum(item['price'] for item in cart_items)
    tax = calculate_tax(subtotal)
    return subtotal + tax

def process_payment(user_id, cart_items):
    """Processes the final payment for the user."""
    total_amount = calculate_total(cart_items)
    print(f"Successfully charged User {user_id} a total of ${total_amount:.2f}")
    return True

# --- Execution ---
cart = [
    {'item': 'Keyboard', 'price': 100.0},
    {'item': 'Mouse', 'price': 50.0}
]

process_payment(991, cart) 
# Output: Successfully charged User 991 a total of $165.00