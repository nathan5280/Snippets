from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity
)


from auth.models.user import User as UserModel

parser = reqparse.RequestParser()
parser.add_argument('username',
                    type=str,
                    required=True,
                    help="Username is a required field.")

parser.add_argument('password',
                    type=str,
                    required=True,
                    help="Password is a required field.")


# class User(Resource):
#     @classmethod
#     def get(cls, username: str):
#         user = UserModel.find(name=username)
#
#         if user:
#             return {
#                 "id": user.id,
#                 "username": user.name
#             }, 200
#
#         return {
#             "message": f"User: {username} not found."
#         }, 404
#
#     @classmethod
#     def post(cls, username: str):
#         data = parser.parse_args()
#         assert username == data["username"]
#
#         try:
#             user = UserModel(**data)
#             user.save()
#         except Exception as e:
#             raise e


class UserLogin(Resource):
    @classmethod
    def post(cls):
        data = parser.parse_args()

        user = UserModel.find(name=data["username"])

        if user and safe_str_cmp(data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)

            return {
                "access_token": access_token,
                "refresh_token": refresh_token
            }, 200

        return {"message": "Invalid credentials"}, 401


class UserRefresh(Resource):
    @classmethod
    @jwt_refresh_token_required
    def post(cls):
        current_user = get_jwt_identity()

        # Note that this is not a fresh token.  We can check with this
        # and make decisions about what we allow them to do.
        new_token = create_access_token(identity=current_user, fresh=False)

        return{"access_token": new_token}, 200
