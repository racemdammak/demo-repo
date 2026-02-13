# checkout_flow.py
from payment_processor import process_transaction

def handle_user_checkout(cart_items, user_id):
    """
    RECENT CODE: Modified today.
    Calls the legacy 'process_transaction' function.
    """
    total = sum(item['price'] for item in cart_items)
    
    # The fix in ingestor.py will now correctly identify 'process_transaction'
    # instead of 'process_transaction(total, user_id)'
    success = process_transaction(total, user_id)
    
    return {"status": "complete" if success else "failed"}