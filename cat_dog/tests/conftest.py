"""Defines fixtures available to all tests."""

import base64

import flask
import pytest

from cat_dog.app import create_app
from cat_dog.settings import TestingConfig


@pytest.yield_fixture(scope='function')
def app():
    """An application for the tests."""
    _app = create_app(TestingConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


class AuthClient():
    def __init__(self, client, authorization):
        self.client = client
        self.authorization = authorization

    def _set_auth(self, kwargs):
        if self.authorization:
            kwargs.setdefault('headers', {})['Authorization'] = (
                'Basic ' + base64.b64encode(':'.join(self.authorization).encode()).decode()
            )

    def get(self, *args, **kwargs):
        self._set_auth(kwargs)
        return self.client.get(*args, **kwargs)

    def post(self, *args, **kwargs):
        self._set_auth(kwargs)
        return self.client.post(*args, **kwargs)

    def post_json(self, *args, **kwargs):
        kwargs['data'] = flask.json.dumps(kwargs['data'])
        kwargs['content_type'] = 'application/json'
        return self.post(*args, **kwargs)


@pytest.yield_fixture(scope='function')
def client(app):
    with app.test_client() as client:
        yield AuthClient(client, authorization=app.config.get('HTTPAUTH'))


@pytest.fixture(scope='function')
def client_class(request, client):
    if request.cls is not None:
        request.cls.client = client
