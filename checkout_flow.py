from payment_processor import process_transaction, log_transaction

def handle_user_checkout(user_id, cart_items):
    total = sum(item['price'] for item in cart_items)
    
    result = process_transaction(total, "USD")
    
    if result['status'] == 'success':
        log_transaction(user_id, result)
        return "Checkout Complete"
    
    return "Failed"

def call_payment():
    return process_transaction(500)