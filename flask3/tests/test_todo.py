import pytest
import json
from .conftest import client, todos


def test_post(client, todos):
    response = client.post("/api/v1/todos", json=todos)
    assert response.json['1'] == "text"
    assert response.status_code == 200

def test_get(client, todos):
    response = client.get("/api/v1/todos")
    assert response.json['1'] == "text"
    assert response.status_code == 200
    
def test_delete(client):
    response = client.delete("/api/v1/todos/1")
    assert response.status_code == 204
