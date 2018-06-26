"""
POPO with minimal information about a specific album for an artist.
"""


class Album:
    def __init__(self, *, name: str, year: int):
        self.name = name
        self.year = year
