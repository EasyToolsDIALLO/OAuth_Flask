from datetime import datetime, timedelta
import os


class authResponse(dict):

    def __init__(self, encode_jwt, expression_seconde, isAdmin):

        EXPIRESSECONDS = int(os.environ.get('EXPIRESSECONDS'))

        self.credentials = encode_jwt
        self.expiration_seconde = expression_seconde
        self.isAdmin = isAdmin
