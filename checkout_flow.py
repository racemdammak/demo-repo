# checkout_flow.py
from payment_processor import process_transaction

def handle_user_checkout(items, uid):
    # RECENT CODE
    # Because of the fix in ingestor.py, the engine will now correctly
    # see 'process_transaction' as the target, matching the Legacy unit.
    return process_transaction(100, uid)