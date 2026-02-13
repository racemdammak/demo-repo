from vault import access_secure_data

def request_handler(user_token):
    # This is our RECENT function calling legacy code
    return access_secure_data(user_token)