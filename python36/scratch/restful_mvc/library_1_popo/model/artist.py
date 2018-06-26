"""
POPO with minimal information about an artist.
"""
from typing import List
from model.album import Album


class Artist:
    def __init__(self, *, name: str, albums: List[Album] = None):
        self.name = name
        self.albums = albums if albums else []
