from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from res.security import authenticate, identity
from res.UserRegister import UserRegister
from res.Item import Item
from res.ItemList import ItemList

def main():
    app = Flask(__name__)
    app.secret_key = 'simple_store'  # Should be hidden in production application.
    api = Api(app)

    JWT(app, authenticate, identity)  # Created new end point called /auth  This will call methods in security

    api.add_resource(Item, '/item/<string:name>')
    api.add_resource(ItemList, '/items')
    api.add_resource(UserRegister, '/register')

    app.run(debug=True, port=5000)

if __name__ == '__main__':
    main()