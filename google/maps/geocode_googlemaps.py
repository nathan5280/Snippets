import json
import os
from pathlib import Path

from googlemaps import Client

with Path(os.environ['GOOGLE_MAPS_API_KEY']).open('rt') as fp:
    key = json.load(fp)['api_key']

client = Client(key=key)

geocode = client.geocode(address="1600 Amphitheatre Parkway, Mountain View, CA")

print(geocode)