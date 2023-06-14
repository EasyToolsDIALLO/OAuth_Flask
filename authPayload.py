from datetime import datetime, timedelta
import os


class authPayload(dict):

    def __init__(self, id, clientId, isAdmin):

        EXPIRESSECONDS = int(os.environ.get('EXPIRESSECONDS'))

        # set the id of the object from Postgres
        self.id = id

        #  The client id (like the user id)
        self.username = clientId

        self.isAdmin = isAdmin

        # set the expiry attrbute
        self.exp = datetime.utcnow() + timedelta(seconds=EXPIRESSECONDS)
