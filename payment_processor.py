# payment_processor.py

def process_transaction(amount, currency="USD"):
    """
    Handles the raw logic for currency conversion.
    RISK: If currency is not a string, this will crash silently in the background worker.
    """
    print(f"Processing {amount} in {currency}...")
    # Simulated logic
    return {"status": "success", "amount": amount}

def log_transaction(tx_id, data):
    """Logs transaction to a global dict (Simulated Memory Leak)"""
    if not hasattr(log_transaction, "_cache"):
        log_transaction._cache = []
    log_transaction._cache.append(data) # This grows forever!
    return True