# checkout_flow.py
from payment_processor import process_transaction

def handle_user_checkout(cart_items, user_id):
    """
    RECENT CODE: Modified < 30 days ago.
    This function must call the legacy function to trigger a conflict.
    """
    total = sum(item['price'] for item in cart_items)
    
    # This direct call creates the dependency (edge) the engine looks for
    result = process_transaction(total, user_id)
    
    return {
        "status": "success" if result else "failed",
        "total": total
    }