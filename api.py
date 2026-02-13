from vault import access_secure_data

def request_handler(user_token):
    return access_secure_data(user_token)