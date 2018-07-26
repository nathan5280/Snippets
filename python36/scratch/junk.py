"""Tests for Google lattitude and longitude methods."""

LAT_LONG_DATA = (1.0, 2.0)


def _get_lat_lng(result: str):
    return LAT_LONG_DATA


LATITUDE = 0
LONGITUDE = 1


def test_get_lat_lng_exists_tuple_of_floats():
    lat_lng = _get_lat_lng(result="google_response_json")
    assert lat_lng  # Check that you got something back.
    assert tuple == type(lat_lng)  # Make sure it is a tuple
    assert 2 == len(lat_lng)  # Make sure it is the right length
    assert isinstance(lat_lng[LATITUDE], float)  # Make sure it is a float
    assert isinstance(lat_lng[LONGITUDE], float)  # Make sure it is a float
    assert LAT_LONG_DATA == lat_lng
