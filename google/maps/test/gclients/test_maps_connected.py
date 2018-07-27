from typing import Callable

import pytest
from data.data_mgr import DataMgr
from gclients import Keys


@pytest.mark.connected
def test_connect_good_location_pass(data_mgr: DataMgr, maps_client_factory: Callable):
    # given
    maps_client = maps_client_factory()

    # when
    location = maps_client.get_location(address=data_mgr.address_good)

    # then
    assert location
    assert data_mgr.location_good == location


@pytest.mark.connected
def test_connect_bad_location_fail(data_mgr: DataMgr, maps_client_factory: Callable):
    # given
    maps_client = maps_client_factory()

    # when
    location = maps_client.get_location(address=data_mgr.address_bad)

    # then
    assert not location


@pytest.mark.connected
def test_bad_api_key_fail(monkeypatch, data_mgr: DataMgr, maps_client_factory: Callable):
    # given
    def bad_key():
        return "bad-key"

    monkeypatch.setattr(Keys, 'get_key', bad_key)

    # when
    with pytest.raises(ValueError):
        maps_client = maps_client_factory()

    # then
