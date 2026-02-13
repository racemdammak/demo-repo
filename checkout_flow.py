# checkout_flow.py
from payment_processor import process_transaction

def handle_user_checkout(items, uid):
    return process_transaction(100, uid)