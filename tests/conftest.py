import pytest


def pytest_addoption(parser):
    parser.addoption("--host", action="store", default="localhost")
    parser.addoption("--port", action="store", default="6000")


@pytest.fixture(scope='session')
def app_url(pytestconfig):
    host = pytestconfig.getoption("host")
    port = pytestconfig.getoption("port")
    return f'http://{host}:{port}'
