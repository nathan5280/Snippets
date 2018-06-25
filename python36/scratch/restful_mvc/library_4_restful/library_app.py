from flask import Flask
from flask_restful import Api

from resource.artist import Artists, ArtistsList


class LibraryApp:
    def __init__(self):
        self.app = Flask(__name__)
        self._api = Api(self.app)

        self._api.add_resource(Artists, '/library/artists/<string:name>')
        self._api.add_resource(ArtistsList, '/library/artists')


if __name__ == '__main__':
    app.run(port=5000, debug=True)