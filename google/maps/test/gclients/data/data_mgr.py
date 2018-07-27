import json
from pathlib import Path

from gclients.maps import Location


class DataMgr:
    GOOD_LOCATION_FILE = "maps/test/gclients/data/good_location.json"

    def __init__(self):
        self.address_good = "1600 Amphitheatre Parkway, Mountain View, CA"
        self.address_bad = "Somewhere not on Earth"

        with Path(self.GOOD_LOCATION_FILE).open('rt') as fp:
            data = json.load(fp)
            self.location_good = Location(**data)

    def save_good_location(self, *, location: Location):
        with Path(self.GOOD_LOCATION_FILE).open('wt') as fp:
            location_dict = {'latitude':location.latitude, 'longitude':location.longitude}
            json.dump(obj=location_dict, fp=fp, indent=4)
            self.address_good = location
