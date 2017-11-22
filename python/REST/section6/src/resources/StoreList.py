from flask_restful import Resource
from models.StoreModel import StoreModel


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
