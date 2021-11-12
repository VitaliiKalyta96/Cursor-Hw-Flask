import pytest
import json
from .conftest import *


def test_plant_get(test_client, plant):
    response = test_client.get('/api/v1/plants')
    response_data = response.get_json()
    assert response_data['location'] == plant.location
    assert response_data['name'] == plant.name
    assert response.status_code == 200
    
def test_post_plant_validations(test_client):
    response = test_client.post(
        '/api/v1/plants',
        data=json.dumps(dict()),
        content_type='application/json'
    )
    errors = response.get_json()
    assert len(errors.keys()) == 2
    assert 'location' in errors.keys()
    assert 'name' in errors.keys()

    response = test_client.post(
        '/api/v1/plants',
        data=json.dumps({
            'name': 'admin'
        }),
        content_type='application/json'
    )
    errors = response.get_json()
    assert len(errors.keys()) == 1
    
 def test_plant_single_resource(test_client, data_id):
    response = test_client.post(
        '/api/v1/plants',
        data=json.dumps(data_id),
        content_type='application/json'
    )
    response_data = response.get_json()
    assert response.status_code == 200
    assert 'id' in response_data
    assert response_data['name'] == data_id['name']
