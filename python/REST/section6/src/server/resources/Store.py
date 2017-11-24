from flask_restful import Resource
from server.models.StoreModel import StoreModel


class Store(Resource):
    @staticmethod
    def get(name):
        store = StoreModel.find_by_name(name)

        if store:
            return store.json(), 200

        return {'message': 'Store not found'}, 404

    @staticmethod
    def post(name):
        if StoreModel.find_by_name(name):
            return {'message': "Store already exists."}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
            return store.json(), 200
        except:
            return {'message': 'An error occured while creating the store.'}, 500

    @staticmethod
    def delete(name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db(name)

        return {'message': 'Store delete'}, 200
