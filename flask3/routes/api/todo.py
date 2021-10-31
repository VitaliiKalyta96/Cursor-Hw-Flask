from app import app, api
from flask import request
from flask_restful import Resource

todos = []


class Todo(Resource):
    def get(self):
        return todos

    def post(self):
        todos.append(request.json)
        return todos

# Створив окермий клас для вирішення 1 завадння 15 дз. Чи я на вірному шляху ?
# Гуглив однак там в методи класу додають переважно ід чи тут потрібно також ід чи потрібно через title??
#

class Todo2(Resource):

    def get(self, title):
        user = get_user_by_data(title)
        if not user:
            return {"error": "User not found"}
        return user
        
    def put(self, title):
        user = get_user_by_data(title)
        if user:
            todos.remove(user)
            todos.append(request.json)
        return todos        

    def delete(self, title):
        return delete_todo()
        user = get_user_by_data(title)
        if user:
            todos.remove(user)
        return {"message": "Deleted"}


# Створив функцію для діставання title для редагування і видалення даних.
# Чи варто її створювати чи є якийсь інший шлях для доступу до даних ???

def get_user_by_data(user_data):
    for x in todos:
        if x.get("title") == int(user_data):
            return x
        
api.add_resource(Todo, "/api/v1/todos")
api.add_resource(Todo2, "/api/v1/todos/<string:title>", methods=['PUT', 'DELETE'])
