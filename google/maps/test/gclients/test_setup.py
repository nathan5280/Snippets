from typing import Callable

import pytest
from data.data_mgr import DataMgr


@pytest.mark.setup
def test_setup_good_location(data_mgr: DataMgr, maps_client_factory: Callable):
    """Get the good location from Google and save it for disconnnected tests."""
    maps_client = maps_client_factory()
    location_good = maps_client.get_location(address=data_mgr.address_good)
    data_mgr.save_good_location(location=location_good)
