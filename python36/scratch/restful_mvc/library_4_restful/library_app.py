from flask import Flask
from flask_restful import Api

from resource.albums import Albums, AlbumsList
from resource.artists import Artists, ArtistsList


class LibraryApp:
    def __init__(self):
        self.app = Flask(__name__)
        self._api = Api(self.app)

        self._api.add_resource(ArtistsList, '/library/artists')
        self._api.add_resource(Artists, '/library/artists/<string:artist_name>')
        self._api.add_resource(AlbumsList, '/library/albums')
        self._api.add_resource(Albums, '/library/albums/<string:artist_name>/<string:album_name>')


if __name__ == '__main__':
    library_app = LibraryApp()
    library_app.app.run(port=5000, debug=True)
