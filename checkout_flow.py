# checkout_flow.py
from payment_processor import process_transaction, log_transaction

def handle_user_checkout(user_id, cart_items):
    """
    Orchestrates the checkout.
    ARCHITECTURAL FLAW: Calls log_transaction without a cleanup strategy.
    """
    total = sum(item['price'] for item in cart_items)
    
    # Passing raw user input directly to the dependency
    result = process_transaction(total, "USD")
    
    if result['status'] == 'success':
        log_transaction(user_id, result)
        return "Checkout Complete"
    
    return "Failed"