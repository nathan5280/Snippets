import pytest
from pytest_mock import mocker
from mocking.model import Model


# Mocking a method in a class.   Because of the fakeness of this example just ignore the self param.
def mock_request(_, *, input: str):
    return "cba"


class Base:
    def simple_request(self):
        # given
        model = Model()
        input = "123"

        # when
        result = model.request(input=input)

        # then
        assert "321" == result

    def longer_request(self):
        # given
        model = Model()
        input = "123-abc"

        # when
        result = model.request(input=input)

        # then
        assert "cba-321" == result


@pytest.mark.mock
class TestMock(Base):
    def test_mock_simple_request(self, mocker):
        mocker.patch('base_test.Model.request', return_value='cba')
        # mocker.patch('base_test.Model.request', mock_request)

        self.simple_request()

    def test_mock_longer_request(self):
        self.longer_request()


@pytest.mark.full
class TestReal(Base):
    def test_full_simple_request(self):
        self.simple_request()

    def test_full_longer_request(self):
        self.longer_request()
