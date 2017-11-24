import sqlite3

from flask_restful import Resource, reqparse

from server.models.UserModel import User


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='This field cannot be blank.')
    parser.add_argument('password', type=str, required=True, help='This field cannot be blank.')

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "User already exists"}, 400

        user = User(**data)
        user.save_to_db()

        return {"message": "User created successfully"}, 201
