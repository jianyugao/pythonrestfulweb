# project/token.py

from itsdangerous import URLSafeTimedSerializer

#from project import app
import config

# def generate_confirmation_token(email):
#     serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
#     return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])


# def confirm_token(token, expiration=3600):
#     serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
#     try:
#         email = serializer.loads(
#             token,
#             salt=app.config['SECURITY_PASSWORD_SALT'],
#             max_age=expiration
#         )
#     except:
#         return False
#     return email

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(config.BaseConfig['SECRET_KEY'])
    return serializer.dumps(email, salt=config.BaseConfig['SECURITY_PASSWORD_SALT'])


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(config.BaseConfig['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=config.BaseConfig['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email