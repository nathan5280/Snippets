# Example of how to request geocodes using low-level requests library.

# import requests
#
# from maps import Location
# from maps.key import get_key
#
#
# class Maps:
#     GEOCODE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
#
#     @classmethod
#     def get_lat_long(cls, *, address: str) -> Location:
#         key = get_key()
#         params = {
#             'address': address,
#             'key': key
#         }
#
#         result = requests.get(cls.GEOCODE_URL, params=params)
#         data = result.json()
#
#         loc = data['results'][0]['geometry']['location']
#         return Location(latitude=loc['lat'], longitude=loc['lng'])
