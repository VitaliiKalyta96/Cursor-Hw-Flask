import pytest
from app import *
from flask import Flask, Response


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
        

@pytest.fixture
def todos():
    yield {
        "title_id": 1,
        "text": "hello"
    }
