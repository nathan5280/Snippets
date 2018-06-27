from werkzeug.security import safe_str_cmp
from auth.models.user import User


def authenticate(user_name, password):
    user = User.find(name=user_name)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    id = payload['identity']
    return User.find(id_=id)
