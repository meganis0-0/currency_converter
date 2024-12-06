from rest_framework_simplejwt.tokens import AccessToken

def create_jwt_token(user):
    return str(AccessToken.for_user(user))

def decode_jwt_token(token):
    return AccessToken(token)