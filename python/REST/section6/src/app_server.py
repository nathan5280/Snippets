from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from server.resources.Store import Store
from server.resources.StoreList import StoreList
from server.resources.Item import Item
from server.resources.ItemList import ItemList
from server.resources.User import UserRegister
from server.util.security import authenticate, identity
from server.util.db import db, DBMgr


def main():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'simple_store'  # Should be hidden in production application.
    api = Api(app)

    # Import here to avoid circular import?
    db.init_app(app)

    # Leverage flask to call this method before handling any requests.
    @app.before_first_request
    def create_tables():
        db.create_all()

    JWT(app, authenticate, identity)  # Created new end point called /auth  This will call methods in security

    api.add_resource(Store, '/store/<string:name>')
    api.add_resource(StoreList, '/stores')

    api.add_resource(Item, '/item/<string:name>')
    api.add_resource(ItemList, '/items')

    api.add_resource(UserRegister, '/register')

    # Clear the DB to support testing.
    api.add_resource(DBMgr, '/clear')

    app.run(debug=True, port=5000)


if __name__ == '__main__':
    main()
