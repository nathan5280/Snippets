from controller.albums import Albums
from controller.artists import Artists


class Library:

    def __init__(self):
        self.artists = Artists()
        self.albums = Albums()
