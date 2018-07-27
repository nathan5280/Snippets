from typing import Callable, Union

from pytest import fixture

from gclients.maps import Location, Maps
from data.data_mgr import DataMgr


def good_mock_return(*, address: str) -> Union[Location, None]:
    data_mgr = DataMgr()
    if data_mgr.address_good == address:
        return data_mgr.location_good

    return None


def fail_mock_return(*, address: str) -> Union[Location, None]:
    return None


@fixture
def data_mgr() -> DataMgr:
    return DataMgr()


@fixture
def maps_client_factory(monkeypatch) -> Callable:
    def _get_maps_client(*, connected: bool = True, good: bool = None) -> Maps:
        client = Maps()

        if not connected:
            if good:
                monkeypatch.setattr(client, 'get_location', good_mock_return)

            else:
                monkeypatch.setattr(client, 'get_location', fail_mock_return)

        return client

    return _get_maps_client

