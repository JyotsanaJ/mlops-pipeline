import pytest
from starlette.testclient import TestClient
from main import app
import json
import pathlib


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client

@pytest.fixture(autouse=True)
def test_body(request):
    file = pathlib.Path(request.node.fspath)
    # print('current test file:', file)
    config = file.with_name('body.json')
    # print('current config file:', config)
    with config.open() as fp:
        test_body = json.loads(fp.read())
    return test_body


@pytest.fixture(autouse=True)
def test_response(request):
    file = pathlib.Path(request.node.fspath)
    # print('current test file:', file)
    config = file.with_name('response.json')
    # print('current config file:', config)
    with config.open() as fp:
        test_response = json.loads(fp.read())
    return test_response