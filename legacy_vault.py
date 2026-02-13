def process_v1_payment(amount):
    # Old logic: no validation, hardcoded tax
    tax = amount * 0.05
    return amount + tax