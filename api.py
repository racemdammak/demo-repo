from vault import access_secure_data

def request_handler(user_token):
    # This is our RECENT function calling legacy code
    # Ensure there are NO spaces in the call for now to help the parser
    return access_secure_data(user_token)