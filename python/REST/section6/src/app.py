from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.Store import Store
from resources.StoreList import StoreList
from resources.Item import Item
from resources.ItemList import ItemList
from resources.User import UserRegister
from util.security import authenticate, identity


def main():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'simple_store'  # Should be hidden in production application.
    api = Api(app)

    # Import here to avoid circular import?
    from util.db import db
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

    app.run(debug=True, port=5000)


if __name__ == '__main__':
    main()
