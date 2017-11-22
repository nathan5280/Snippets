class User:
    def __init__(self, identifier, username, password):
        self._identifier = identifier
        self._username = username
        self._password = password

    @property
    def id(self):
        return self._identifier

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password
