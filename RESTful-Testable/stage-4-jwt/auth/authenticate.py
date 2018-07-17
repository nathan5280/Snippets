from werkzeug.security import safe_str_cmp
from auth.user import User


# Methods required by flask_jwt
def authenticate(username, password):
    """Authenticate a user with their password."""
    user = User.find(username=username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    """Find a user by their ID."""
    id_ = payload['identity']
    return User.find(id_=id_)
