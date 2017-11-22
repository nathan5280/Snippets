from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.ItemModel import ItemModel
from util.exceptions import ItemAlreadyExistsStoreException


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='price field required.')
    parser.add_argument('store_id', type=int, required=True, help='store_id field required.')

    @staticmethod
    def post(name):  # Create
        data = Item.parser.parse_args()

        try:
            item = ItemModel(name, data['price'], data['store_id'])

            item.save_to_db()
            # Everything is good.
            return item.json(), 201

        except ItemAlreadyExistsStoreException as e:
            # Client tried to create an item that already exists.
            return {'message': e.__str__()}, 400

    @staticmethod
    @jwt_required()  # If this is applied then the header of the call needs to include Authorization=JWT <token>
    def get(name):  # Read
        item = ItemModel.find_by_name(name)
        if item:
            # Everything is good.
            return item.json(), 200

        # Item not found.
        return {'message': "Item '{}' not found.".format(name)}, 400

    @staticmethod
    def put(name):  # Update
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        if item:
            if 'price' in data.keys():
                item.price = data['price']

            if 'name' in data.keys():
                item.name = data['name']

            if 'store_id' in data.keys():
                item.name = data['store_id']
        else:
            item = ItemModel(name, data['price'], data['store_id'])

        item.save_to_db()

        return item.json(), 201

    @staticmethod
    def delete(name):  # Delete
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db(name)

        return {'message': 'Item deleted'}, 200
