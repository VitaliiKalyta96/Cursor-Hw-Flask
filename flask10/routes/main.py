from app import app, db
from flask import render_template, request, redirect, url_for, session
from models import Plant, Employee, Salon


@app.route('/')
def main():
    plants = Plant.query.all()
    employees = Employee.query.all()
    salons = Salon.query.all()
    return render_template('index.html', plants=plants, employees=employees, salons=salons, session=session)


@app.route('/plant/<int:id>')
def plant(id):
    plant = Plant.query.get(id)
    employees = Employee.query.all()
    return render_template('edit-plant.html', plant=plant, employees=employees, session=session)


@app.route('/login')
def login():
    return render_template('f.html', session=session)


@app.route('/auth', methods=['POST'])
def auth():
    form = request.form
    user = Employee.query.filter(Employee.email == form['login']).filter(Employee.password == form['password']).first()
    print("Hello AUTH:")
    print(user)
    if user is not None:
        session['user'] = user.serialize
    return redirect("http://localhost:8082/")


@app.route('/plant/<int:id>/edit')
def plant_edit_page(id):
    plant = Plant.query.get(id)
    employees = Employee.query.all()
    return render_template('edit-plant.html', plant=plant, employees=employees, salon=salon, session=session)


@app.route('/plant/<int:id>/update', methods=['POST'])
def plant_update(id):
    plant = Plant.query.get(id)
    form_data = request.form
    plant.name = form_data.get('name')
    plant.location = form_data.get('location')
    plant.director_id = form_data.get('director_id')
    db.session.add(plant)
    db.session.commit()
    return redirect(url_for('plant', id=id))


@app.route('/employee/<int:id>')
def employee(id):
    employee = Employee.query.get(id)
    return render_template('employee.html', employee=employee, session=session)


@app.route('/employee/<int:id>/edit')
def employee_edit_page(id):
    employee = Employee.query.get(id)
    plants = Plant.query.all()
    salons = Salon.query.all()
    return render_template('edit-employee.html', plants=plants, employee=employee, salons=salons, session=session)


@app.route('/employee/<int:id>/update', methods=['POST'])
def employee_update(id):
    employee = Employee.query.get(id)
    form_data = request.form
    employee.email = form_data.get('email')
    employee.name = form_data.get('name')
    employee.department_type = form_data.get('department_type')
    employee.department_id = form_data.get('department_id')
    db.session.add(employee)
    db.session.commit()
    return redirect(url_for('employee', id=id))


@app.route('/salon/<int:id>')
def salon(id):
    salon = Salon.query.get(id)
    return render_template('salon.html', salon=salon, session=session)


@app.route('/salon/<int:id>/update', methods=['POST'])
def salon_update(id):
    salon = Salon.query.get(id)
    form_data = request.form
    employee.name = form_data.get('name')
    employee.city = form_data.get('city')
    employee.address = form_data.get('address')
    db.session.add(salon)
    db.session.commit()
    return redirect(url_for('salon', id=id))
