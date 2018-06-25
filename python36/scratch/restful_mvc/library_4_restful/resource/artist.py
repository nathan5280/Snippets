from flask_restful import Resource
from controller.session_scope import session_scope
from controller.exc import NotFoundException
from controller.library import Library


class Artists(Resource):
    def __init__(self):
        self.library = Library()

    def get(self, name):
        with session_scope():
            print("\tArtist.get")
            try:
                artist = self.library.artists.read(name=name)
                return artist.json()
            except NotFoundException as e:
                return {"message": str(e)}, 400


class ArtistsList(Resource):
    def __init__(self):
        self.library = Library()

    def get(self):
        with session_scope():
            print("\tArtistsList.get")
            artists = self.library.artists.list()
            return {
                "artists": [artist.json() for artist in artists]
            }
