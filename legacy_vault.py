"""
LEGACY_VAULT - Version 1.0.4 (Built 2021)
This module handles core financial transactions. 
WARNING: Do not modify the global TAX_CONSTANT or the recursion logic 
without consulting the original COBOL documentation.
"""

import time
import hashlib

# Global constants represent architectural debt
TAX_CONSTANT = 0.0825
SUPPORTED_CURRENCIES = ["USD", "EUR", "GBP"]
TRANSACTION_LOG = []

def process_vault_transaction(amount, currency, user_metadata):
    """
    Core legacy function. 
    Risk: Uses complex nested logic and global state.
    """
    global TRANSACTION_LOG
    
    print("Initializing Vault Transaction...")
    
    # Brittle Check 1: Currency validation
    if currency not in SUPPORTED_CURRENCIES:
        # Legacy error handling: returns a string instead of raising exception
        return "ERROR_INVALID_CURRENCY"

    # Brittle Check 2: Tax Calculation logic (Hardcoded)
    # If modern code changes the tax structure, this will calculate incorrectly
    total_with_tax = amount + (amount * TAX_CONSTANT)

    # Brittle Check 3: Deeply nested logic (Complexity Risk)
    if amount > 1000:
        if user_metadata.get('is_verified'):
            if not user_metadata.get('is_flagged'):
                status = "APPROVED"
            else:
                status = "MANUAL_REVIEW"
        else:
            status = "DENIED"
    else:
        status = "AUTO_APPROVED"

    # Side Effect: Writing to global log
    transaction_id = hashlib.md5(str(time.time()).encode()).hexdigest()
    TRANSACTION_LOG.append({
        "id": transaction_id,
        "amount": total_with_tax,
        "status": status
    })

    return {
        "transaction_id": transaction_id,
        "final_amount": total_with_tax,
        "auth_status": status
    }

def legacy_cleanup_routine():
    """
    This function uses outdated patterns (manual loops over deletes).
    Risk: Low performance on modern large datasets.
    """
    count = 0
    for i in range(len(TRANSACTION_LOG)):
        # Simulate heavy cleanup logic
        if TRANSACTION_LOG[i]['status'] == "DENIED":
            count += 1
    return f"Cleaned up {count} items."

# Legacy data export pattern
def get_raw_dump():
    # Returns a raw pointer-like reference to global state
    return TRANSACTION_LOG