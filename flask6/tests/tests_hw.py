import pytest
import json
from models.models import Plant, Employee, MenuItem, Salon
from app import app, db
from .conftest import *


def test_plant_post(client, plant_data):
    plant_1 = Plant(
        'location': 'Ternopil',
        'name': 'Jacktom'
    )
    response = client.post("/api/v1/plants", json=plant_data)
    assert response.status_code == 200
    
def test_plant_get(client, plant_data):
    response = client.get("/api/v1/plants")
    assert response.status_code == 200
    assert ('Ternopil', str(response.data))
    
def test_plant_get_id(client, plant_data):
    response = client.get("/api/v1/plants/1")
    assert response.status_code == 200
    assert ('Jacktom', str(response.data))
    
def test_plant_delete(client):
    response = client.delete("/api/v1/plants/1")
    assert response.status_code == 204
    response = client.delete("/api/v1/plants/1")
    assert response.status_code == 404
    
    
def test_employee_post(client, employee_data):
    employee_1 = Employee(
        'email': 'jack@gmail.com',
        'name': 'Jack',
        'department_type': 'technic'
    )
    response = client.post("/api/v1/employees", json=employee_data)
    assert response.status_code == 200

def test_employee_get(client, employee_data):
    response = client.get("/api/v1/employees")
    assert response.status_code == 200
    assert ('jack@gmail.com', str(response.data)
    
def test_employee_get_id(client, employee_data):
    response = client.get("/api/v1/plants/1")
    assert response.status_code == 200
    assert ('Jack', str(response.data))
    
def test_employee_delete(client):
    response = client.delete("/api/v1/employees/1")
    assert response.status_code == 204
    response = client.delete("/api/v1/employees/1")
    assert response.status_code == 404

    
def test_menuitem_post(client, menuitem_data):
    menuitem_1 = MenuItem(
        'name': 'Plant_Employee_Salon',
        'link': 'menu'
    )
    response = client.post("/api/v1/menu-items", json=menuitem_data)
    assert response.status_code == 200
    
def test_menuitem_get(client, menuitem_data):
    response = client.get("/api/v1/menu-items")
    assert response.status_code == 200
    assert ('menu', str(response.data))
    
def test_menuitem_get_id(client, menuitem_data):
    response = client.get("/api/v1/menu-items/1")
    assert response.status_code == 200
    assert ('Plant_Employee_Salon', str(response.data))
    
def test_menuitem_delete(client):
    response = client.delete("/api/v1/menu-items/1")
    assert response.status_code == 204
    response = client.delete("/api/v1/menu-items/1")
    assert response.status_code == 404   


def test_salon_post(client, salon_data):
    salon_1 = Salon(
        'name': 'Roy',
        'city': 'Lviv',
        'address': 'Washington street 20'
    )
    response = client.post("/api/v1/salons", json=salon_data)
    assert response.status_code == 200
    
def test_salon_get(client, salon_data):
    response = client.get("/api/v1/salons")
    assert response.status_code == 200
    assert ('Roy', str(response.data))
    
def test_salon_get_id(client, salon_data):
    response = client.get("/api/v1/salons")
    assert response.status_code == 200
    assert ('Lviv', str(response.data))
    
def test_salon_delete(client):
    response = client.delete("/api/v1/salons/1")
    assert response.status_code == 204
    response = client.delete("/api/v1/salons/1")
    assert response.status_code == 404


