from legacy_vault import process_v1_payment

def checkout(cart_total):
    # Calling legacy code from 2024
    final_price = process_v1_payment(cart_total)
    print(f"Total: {final_price}")