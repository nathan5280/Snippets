import pytest
from data.data_mgr import DataMgr

from gclients.maps import Location

ADDRESS_GOOD = "1600 Amphitheatre Parkway, Mountain View, CA"
LOCATION_GOOD = Location(latitude=37.42267, longitude=-122.0845544)

ADDRESS_BAD = "Somewhere not on Earth"


@pytest.mark.infrastructure
def test_load():
    # given
    data_mgr = DataMgr()

    # when
    # then
    assert ADDRESS_GOOD == data_mgr.address_good
    assert LOCATION_GOOD == data_mgr.location_good
    assert ADDRESS_BAD == data_mgr.address_bad


@pytest.mark.infrastructure
def test_save():
    # given
    data_mgr = DataMgr()

    location_bad = Location(latitude=0.0, longitude=0.0)

    location_save = data_mgr.location_good

    # when
    data_mgr.save_good_location(location=location_bad)
    data_mgr = DataMgr()
    location_bad_saved = data_mgr.location_good

    # then
    assert location_bad == location_bad_saved

    # Clean things up.
    data_mgr.save_good_location(location=location_save)