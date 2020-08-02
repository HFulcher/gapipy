import pytest
from gapipy.client import (authenticate, _authenticate_service,
                           _authenticate_install, _build, Client)


@pytest.fixture
def mock_authenticate(monkeypatch):
    def mock_authenticate_service(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(authenticate, "_authenticate_service", mock_authenticate_service)


def test_authenticate_service_file():
    assert True

def test_authenticate_service_nofile():
    assert True


def test_authenticate_install_file():
    assert True

def test_authenticate_install_env():
    assert True