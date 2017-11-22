from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from res.ItemList import ItemList
from res.exceptions import WrappedStoreException, ItemNotFoundStoreException, \
    ItemAlreadyExistsStoreException, BaseStoreException


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='price field required.')

    # @staticmethod
    # @jwt_required()
    @staticmethod
    def get(name):
        try:
            item = ItemList.find_by_name(name)
            if item:
                # Everything is good.
                return item, 200
            else:
                # Item not found.
                return {'message': "Item '{}' not found.".format(name)}, 400

        except Exception as e:
            # Server error.
            return {'message': e.__str__()}, 500

    @staticmethod
    def post(name):
        try:
            data = Item.parser.parse_args()
            item = {'name': name, 'price': data['price']}

            ItemList.save_to_db(name, item)
            # Everything is good.
            return item, 201

        except ItemAlreadyExistsStoreException as e:
            # Client tried to create an item that already exists.
            return {'message': e.__str__()}, 400

        except Exception as e:
            # Server error.
            return {'message': e.__str__()}, 500

    @staticmethod
    def delete(name):
        try:
            ItemList.delete_from_db(name)
            # Everything is good.
            return {}, 200

        except ItemNotFoundStoreException:
            # It didn't exist so we can't delete it, but it isn't an error.
            # Everything is good.
            return {}, 200

        except Exception as e:
            # Server Error.
            return {'message': e.__str__()}, 500

    @staticmethod
    def put(name):
        try:
            data = Item.parser.parse_args()
            item = {'name': name, 'price': data['price']}

            # New Item
            ItemList.update(name, item)
            # Everything is good.
            return item, 201

        except Exception as e:
            return {'message': e.__str__()}, 500
