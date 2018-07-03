from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token

from auth.models.user import User


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="Username is a required field.")

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="Password is a required field.")

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()

        user = User.find(name=data["username"])

        if user and safe_str_cmp(data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)

            return {
                "access_token": access_token,
                "refresh_token": refresh_token
            }, 200

        return {"message": "Invalid credentials"}, 401
