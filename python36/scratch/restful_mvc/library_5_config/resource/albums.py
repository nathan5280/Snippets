from flask import request
from flask_restful import Resource, reqparse

from controller.exc import NotFoundException, AlreadyExistsException
from controller.library import Library
from controller.session_scope import session_scope
from model.artist import Artist as ArtistModel
from model.album import Album as AlbumModel


class Albums(Resource):
    req_parser = reqparse.RequestParser()
    req_parser.add_argument('year',
                            type=int,
                            required=True,
                            help="year field required.")

    def __init__(self):
        self._library = Library()

    def get(self, artist_name, album_name):
        with session_scope():
            try:
                album = self._library.albums.read(artist_name=artist_name, name=album_name)
                if album:
                    return album.json()
                else:
                    return{"message": f"Artist '{artist_name}', Album '{album_name}' not found in Library.'"}, 404
            except NotFoundException as e:
                return {"message": str(e)}, 404

    def post(self, artist_name, album_name):
        req_data = Albums.req_parser.parse_args()

        album = AlbumModel(name=album_name, year=req_data["year"])
        with session_scope():
            try:
                self._library.albums.create(artist_name=artist_name, album=album)
                return album.json(), 201
            except AlreadyExistsException as e:
                return {"message": str(e)}, 500

    def put(self, artist_name, album_name):
        req_data = Albums.req_parser.parse_args()

        album = AlbumModel(name=album_name, year=req_data["year"])
        with session_scope():
            try:
                self._library.albums.update(artist_name=artist_name, album=album)
                return album.json(), 201
            except NotFoundException as e:
                return {"message": str(e)}, 404

    def delete(self, artist_name, album_name):
        with session_scope():
            self._library.albums.delete(artist_name=artist_name, name=album_name)


class AlbumsList(Resource):
    def __init__(self):
        self._library = Library()

    def get(self):
        with session_scope():
            albums = self._library.albums.list()
            return {
                "albums": [album.json() for album in albums]
            }