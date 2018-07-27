import json
from os import environ
from pathlib import Path


class Keys:
    @staticmethod
    def get_key() -> str:
        """Load the API Key from the file specified in the environment variable."""
        with Path(environ['GOOGLE_MAPS_API_KEY']).open('rt') as fp:
            return json.load(fp)['api_key']
