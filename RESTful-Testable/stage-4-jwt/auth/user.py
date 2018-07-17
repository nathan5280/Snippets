"""User, ID and Password information.  In a production implementation this would be stored externally."""
_user_data = {
    "peter": {
        'id': 1,
        'password': "123"
    },
    "paul": {
        'id': 2,
        'password': "234"
    }
}

# Invert the user information to lookup by ID.
_id_data = {_user_data[username]["id"]: {"username": username,
                                         "password": _user_data[username]["password"]}
            for username in _user_data}


class User:
    """Basic user."""
    def __init__(self, *, username: str, id_: int, password: str):
        self.username = username
        self.id = id_
        self.password = password

    @classmethod
    def find(cls, *, username: str = None, id_: int = None):
        """Find the user in the system by username or id."""
        assert (username or id_) and not (username and id_)

        if username and username in _user_data:
            return cls(username=username, id_=_user_data[username]["id"], password=_user_data[username]["password"])

        if id_ and id_ in _id_data:
            return cls(username=_id_data[id_]["username"], id_=id_, password=_id_data[id_]["password"])

    def __eq__(self, obj):
        eq_keys = ["username", "id", "password"]
        return all([getattr(self, key) == getattr(obj, key) for key in eq_keys])
