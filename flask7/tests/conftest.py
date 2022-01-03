import pytest
from models.models import Plant, Employee, MenuItem, Salon
from app import app, db


@pytest.fixture
def client():
    app.test = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask:flask@db:3306/flask'
    client = app.test_client()
    with app.app_context():
        db.create_all()
        db.session.commit()
    yield client

@pytest.fixture()
def plant_data():
    yield {
        'location': 'Ternopil',
        'name': 'Jacktom'
    }
    
@pytest.fixture()
def employee_data():
    yield {
        'email': 'jack@gmail.com',
        'name': 'Jack',
        'department_type': 'technic'
    } 
        
@pytest.fixture()
def menuitem_data():
    yield {
        'name': 'Plant_Employee_Salon',
        'link': 'menu'
    }

@pytest.fixture()
def salon_data():
    yield {
        'name': 'Roy',
        'city': 'Lviv',
        'address': 'Washington street 20'
    }
