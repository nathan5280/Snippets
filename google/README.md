# Testing Google API with Mock Objects
## Overview
Testing "expensive (Time, $)" resources can be time consuming or expensive ($).  It is helpful to be able to 
stub out these expensive calls in the unit tests to manage this cost.   Python monkeypatching is a way to 
accomplish this without having to build special functionality into code that delivers the functionality.

For this Snippet a simple Maps class is written to query the Google Maps API to convert an address to a
geolocation (latitude and longitude)

## Code
The small amount of functionality that is used to request the address to geocode is located in 
*gclients/maps.py*.  
```python
Location = NamedTuple('Location', [('latitude', float),
                                   ('longitude', float)])


class Maps:
    def __init__(self):
        key = Keys.get_key()
        self.client = Client(key=key)

    def get_location(self, *, address: str) -> Union[Location, None]:
        result = self.client.geocode(address=address)

        if result:
            loc = result[0]['geometry']['location']
            return Location(latitude=loc['lat'], longitude=loc['lng'])
        else:
            return None
```

**Notes**
* The get_location either returns a NamedTuple with the latitude and longitude or None.
* The heavy lifting is done by the googlemaps.Client object.   It handles retries, timeouts and rate limiting.
* API keys are stored in a file that is identified by the environment variable 'GOOGLE_MAPS_API_KEY'.
    ```python
    {
        "api_key": "your-api-key-here"
    }
    ```

## Tests
Tests execution is controlled with pytest.marks.  Custom marks are defined in *google/pytest.ini*
```text
[pytest]
markers =
    connected: Mark a test that connects to Google
    setup: Mark a test that connects to Google and saves the results for other tests.
    infrastructure: Mark a test as testing infrastructure.  Testing of these not needed unless changing the infrastructure.
```

**Marks** can be listed to make sure the pytest.ini file(s) are being picked up.
```commandline
pytest --markers
```

You should see the connected, setup and infrastructure marks listed.

### Test Setup
* Working Directory: google
* PYTHONPATH=. 

### Execution Order
Not all of the tests need to be run all of the time.

* infrastructure
    These tests are for the DataMgr class and really only need to be run with the DataMgr class is being 
    developed.  They can be run by setting additional arguments in PyCharm test configuration.  Ultimately
    you want to run.
    ```commandline
    pytest -v -m "infrastructure"
    ```
    "-v" increases the verbosity of PyTest so you can see exactly which tests were run.
    "-m <mark-condition>" Selects and excludes tests to run based on the marks.  
    
* setup
    These are the test(s) that get the information about what a connected request to Google Maps would return
    and saves it to disk for use with disconnected tests.  These tests should be run whenever the result from
    Google has changed.   In this case it would be if there was an update to the geocode for the good address.
    Hopefully this doesn't happen very often and we can test functionality without having to keep hitting 
    Google everytime we run our tests.
    ```commandline
    pytest -v -m "setup"
    ```    

* connected
    These are the real tests against the Google API.  Running these 100's of times a day could incur some costs.
    We would want to run these tests before we released to production.
    ```commandline
    pytest -v -m "connected"
    ``` 
    
* Everything else
    These are the tests that run against the mock Google Maps API. 
    ```commandline
    pytest -v -m "not infrastructure and not setup and not connected"
    ```

### DataMgr
The DataMgr controls access to the good/bad addresses and locations used by the tests.  It stores the 
good location information for the good address in *maps/test/gclients/data/good_location.json*. This location
information is used when the disconnected tests are run.  The good location information can be updated 
by running the test_setup test.  This test queries google for the good location and saves it to the file using 
the DataMgr. 

### conftest
```python
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
```

Tests are not able to directly pass parameters to test fixtures.  To work around this the test fixture returns
a factor to create the different maps_clients.  The individual tests request a maps_client from the factory
and pass the parameters to tell what type of maps client the test needs.   In this case the factory can generate
three different maps_clients.
1. Connected Maps object that will connect to Google Maps.
1. Disconnected Maps object that returns the good geocode location from the data file.
1. Disconnected Maps object that returns no geocode location.

Within the tests the maps_client is requested as follows.
```python
maps_client = maps_client_factory(connected=False, good=False)
```
When the factory creates the client for connected=False scenerio it monkeypatches the 'get_location' method
in the Maps object with either the good_mock_return() or fail_mock_return() functions.  This allows the tests
to be written against the same Maps object in connected or disconnected modes without having to make any
changes to the underlying Maps code.

### Keys.get_key
A similar monkeypatch is used to test for the ValueError exception that is thrown when the googlemaps.Client is 
constructed with a bad API key.
```python
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
```

Here the Keys.get_key() method is patched to return a bad key which blows up the Client.  Again, the test works
with the unmodified Maps code.