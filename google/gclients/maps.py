from typing import NamedTuple, Union

from googlemaps import Client

from gclients import Keys

Location = NamedTuple('Location', [('latitude', float),
                                   ('longitude', float)])


class Maps:
    def __init__(self):
        """Initialize the Maps object with a connection to the googlemaps.Client"""
        key = Keys.get_key()
        self.client = Client(key=key)

    def get_location(self, *, address: str) -> Union[Location, None]:
        """
        Convert the address to geocode.

        :param address: Address to convert.
        :return: Geocode Location object or None
        """
        result = self.client.geocode(address=address)

        if result:
            loc = result[0]['geometry']['location']
            return Location(latitude=loc['lat'], longitude=loc['lng'])
        else:
            return None
