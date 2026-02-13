from legacy_vault import process_vault_transaction

def handle_web_payment(request):
    # Modern logic trying to interface with the brittle legacy function
    data = request.json()
    
    # RISK: Modern code passing a dictionary structure the legacy 
    # code might not fully validate or handle as expected.
    result = process_vault_transaction(
        amount=data['amt'],
        currency=data['cur'],
        user_metadata=data['user']
    )
    
    return result