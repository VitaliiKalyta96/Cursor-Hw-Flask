from app import app, api
from flask import request
from flask_restful import Resource

todos = []

# Створив функцію для діставання title, text для редагування і видалення даних.
# Чи варто її створювати чи є якийсь інший шлях для доступу до даних ???

def get_user_by_data(user_data):
    for x in todos:
        if x.get("title", "text") == str(user_data):
            return x


class Todo(Resource):
    def get(self):
        return todos

    def post(self):
        todos.append(request.json)
        return todos

# Створив окермий клас для вирішення 1 завадння 15 дз. Чи я на вірному шляху ?
# Гуглив однак там в методи класу додають переважно ід чи тут потрібно також ід чи потрібно через title, text??
#

class Todo2(Resource):

    def get(self, title, text):
        user = get_user_by_data(title, text)
        if not user:
            return {"error": "User not found"}
        return user
        
    def put(self, title, text):
        user = get_user_by_data(title, text)
        if user:
            todos.remove(user)
            todos.append(request.json)
        return todos        

    def delete(self, title, text):
        return delete_todo()
        user = get_user_by_data(title, text)
        if user:
            todos.remove(user)
        return {"message": "Deleted"}
        
api.add_resource(Todo, "/api/v1/todos")
api.add_resource(Todo2, "/api/v1/todos/<str:title>/<str:text>", methods=['PUT', 'DELETE'])
