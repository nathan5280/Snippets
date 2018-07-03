from flask_restful import Resource

from controller.exc import NotFoundException, AlreadyExistsException
from controller.library import Library
from controller.session_scope import session_scope
from model.artist import Artist as ArtistModel


class Artists(Resource):
    def __init__(self):
        self._library = Library()

    def get(self, artist_name):
        with session_scope():
            try:
                artist = self._library.artists.read(name=artist_name)
                return artist.json()
            except NotFoundException as e:
                return {"message": str(e)}, 404

    def post(self, artist_name):
        with session_scope():

            artist = ArtistModel(name=artist_name)
            try:
                self._library.artists.create(artist=artist)
            except AlreadyExistsException as e:
                return {"message": str(e)}, 500

    def delete(self, artist_name):
        with session_scope():

            self._library.artists.delete(name=artist_name)


class ArtistsList(Resource):
    def __init__(self):
        self.library = Library()

    def get(self):
        with session_scope():
            artists = self.library.artists.list()
            return {
                "artists": [artist.json() for artist in artists]
            }
