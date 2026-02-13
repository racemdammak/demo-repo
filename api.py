from vault import access_secure_data

def request(user_token):
    # test legacy & units
    return access_secure_data(user_token)