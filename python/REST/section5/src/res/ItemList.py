from flask_restful import Resource, reqparse
import sqlite3

from res.exceptions import WrappedStoreException, ItemAlreadyExistsStoreException, ItemNotFoundStoreException


class ItemList(Resource):
    @staticmethod
    def create(name, item):
        if ItemList.find_by_name(name):
            raise ItemAlreadyExistsStoreException(name)

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES(?, ?)"
        cursor.execute(query, (name, item['price']))
        connection.commit()
        connection.close()

    @staticmethod
    def find_by_name(name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        else:
            return None

    @staticmethod
    def update(name, item):
        existing_item = ItemList.find_by_name(name)
        if existing_item:
            # Item exists - update
            update_item = {**existing_item, **item}

            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            query = "UPDATE items SET name=?, price=? WHERE name=?"
            cursor.execute(query, (update_item['name'], update_item['price'], update_item['name']))
            connection.commit()
            connection.close()
        else:
            # Item doesn't exist.
            ItemList.create(name, item)

    @staticmethod
    def delete(name):
        if ItemList.find_by_name(name):
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            query = "DELETE FROM items WHERE name=?"
            cursor.execute(query, (name,))
            connection.commit()
            connection.close()

    @staticmethod
    def get():
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = [{'name': r[0], 'price': r[1]} for r in result]

        connection.commit()
        connection.close()

        return {'items': items}

