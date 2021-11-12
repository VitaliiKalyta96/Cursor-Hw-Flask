import os
import pytest

from app import *


os.environ["SQLALCHEMY_DATABASE_URI"] = 'testing'

@pytest.yield_fixture(scope='session')
def app():
    app = app(config_name='testing')

    with app.app_context():
        yield app


@pytest.fixture
def app_context(app):
    with app.app_context() as ctx:
        yield ctx


@pytest.fixture
def test_client(app, app_context):
    return app.test_client()


@pytest.yield_fixture(scope='session')
def db(app):
    with app.app_context():
        db_instance.drop_all()
        db_instance.create_all()
        yield db_instance
