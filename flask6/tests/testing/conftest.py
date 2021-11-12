import pytest
from models.models import Plant, Employee, MenuItem, Salon
from app import *
from flask import Flask, Response


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture()
def plant_data():
    yield {
        'location': 'New York',
        'name': 'Jacktom'
    }
    
@pytest.fixture()
def employee_data():
    yield {
        'email': 'jack@gmail.com',
        'name': 'Jack',
        'department_type': 'technic',
        } 
        
@pytest.fixture()
def menuitem_data():
    yield {
        'name': 'Plant_Employee_Salon',
        'link': 'simple'
        }

@pytest.fixture()
def salon_data():
    yield {
        'name': 'Roy',
        'city': 'Lviv',
        'address': 'Washington street 20'
    }
