def calculate_tax(amount, tax_rate): 
    # BREAKING CHANGE: Added a required 'tax_rate' parameter
    return amount * tax_rate

def calculate_total(cart_items):
    """Calculates the subtotal and adds tax."""
    subtotal = sum(item['price'] for item in cart_items)
    
    # FATAL ERROR: This function is still only passing one argument.
    # It will throw a TypeError: calculate_tax() missing 1 required positional argument: 'tax_rate'
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
# Crashes the program!