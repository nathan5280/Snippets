from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask_restful import Resource

db = SQLAlchemy()


class DBMgr(Resource):
    @staticmethod
    def delete():
        """
        Clear the contents of the database to support testing.

        :return: None
        """
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items"
        cursor.execute(query)

        query = "DELETE FROM stores"
        cursor.execute(query)

        query = "DELETE FROM users"
        cursor.execute(query)

        connection.commit()
        connection.close()

        return {'message': 'DB Cleared'}, 200

