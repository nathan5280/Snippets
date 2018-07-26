import json
import os
from pathlib import Path

import requests

with Path(os.environ['GOOGLE_MAPS_API_KEY']).open('rt') as fp:
    key = json.load(fp)['api_key']

print(f"key: '{key}'")

url = "https://maps.googleapis.com/maps/api/geocode/json"

params = {
    'address': "1600 Amphitheatre Parkway, Mountain View, CA",
    'key': key
}

r = requests.get(url, params=params)

print(f"encoding: {r.encoding}")
print(f"status: {r.status_code}")
print(f"response: {r.json()}")
