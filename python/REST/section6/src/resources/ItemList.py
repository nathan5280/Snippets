from flask_restful import Resource

from models.ItemModel import ItemModel


class ItemList(Resource):
    @staticmethod
    def get():
        return {'items': [item.json() for item in ItemModel.query.all()]}

        # With lambda
        # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}