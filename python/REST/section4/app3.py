from flask import Flask, request
from flask_jwt import JWT, jwt_required
from flask_restful import Resource, Api, reqparse

from util.security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'simple_store'  # Should be hidden in production application.
api = Api(app)

jwt = JWT(app, authenticate, identity)  # Created new end point called /auth  This will call methods in security


class ItemList(Resource):
    @staticmethod
    def get_item(name):
        return items.get(name, dict())

    @staticmethod
    def add_item(name, item):
        items[name] = item

    @staticmethod
    def del_item(name):
        item = ItemList.get_item(name)
        if item:
            del items[name]

    @staticmethod
    def get():
        return items, 200


class Item(Resource):
    @staticmethod
    @jwt_required()
    def get(name):
        item = ItemList.get_item(name)
        return item, 200 if item else 404

    @staticmethod
    def post(name):
        data = request.get_json()

        item = ItemList.get_item(name)
        if item:
            return {'message': "item '{}' already exists.".format(name)}, 400

        item = {
            'price': data['price'],
            'quantity': data['quantity']
        }

        ItemList.add_item(name, item)
        return {name: item}, 201

    @staticmethod
    def delete(name):
        ItemList.del_item(name)
        return {}, 200

    @staticmethod
    def put(name):
        item = ItemList.get_item(name)
        # Item exists
        if item:
            data = request.get_json()

            if 'price' in data.keys():
                item['price'] = data['price']

            if 'quantity' in data.keys():
                item['quantity'] = data['quantity']
        else:
            # New item
            parser = reqparse.RequestParser()
            parser.add_argument('price', type=float, required=True, help='New price for the item.')
            parser.add_argument('quantity', type=float, required=True, help='New quantity for the item.')

            data = parser.parse_args()

            item = {
                'price': data['price'],
                'quantity': data['quantity']
            }

            ItemList.add_item(name, item)

        return {name: item}, 201


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

items = dict()
item_list = ItemList()

app.run(debug=True, port=5000)
