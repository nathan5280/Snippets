from typing import Callable

from data.data_mgr import DataMgr


def test_disconnect_good_location_pass(data_mgr: DataMgr, maps_client_factory: Callable):
    # given
    maps_client = maps_client_factory(connected=False, good=True)

    # when
    location = maps_client.get_location(address=data_mgr.address_good)

    # then
    assert location
    assert data_mgr.location_good == location


def test_disconnect_bad_location_fail(data_mgr: DataMgr, maps_client_factory: Callable):
    # given
    maps_client = maps_client_factory(connected=False, good=False)

    # when
    location = maps_client.get_location(address=data_mgr.address_bad)

    # then
    assert not location