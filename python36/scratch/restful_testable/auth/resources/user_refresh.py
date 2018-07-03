from flask_jwt_extended import (
    create_access_token, jwt_refresh_token_required, get_jwt_identity
)
from flask_restful import Resource, reqparse


class UserRefresh(Resource):
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
    @jwt_refresh_token_required
    def post(cls):
        current_user = get_jwt_identity()

        # Note that this is not a fresh token.  We can check with this
        # and make decisions about what we allow them to do.
        new_token = create_access_token(identity=current_user, fresh=False)

        return{"access_token": new_token}, 200
