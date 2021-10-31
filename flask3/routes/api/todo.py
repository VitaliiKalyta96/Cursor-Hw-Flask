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
        
        
def get_by_data(data):
    for x in todos:
        if x.get("title") == str(data):
            return x


class Todo2(Resource):

    def get(self, title):
        user = get_by_data(title)
        if not user:
            return {"error": "User not found"}
        return user
        
    def put(self, title):
        user = get_by_data(title)
        if user:
            todos.remove(user)
            todos.append(request.json)
        return todos        

    def delete(self, title):
        return delete_todo()
        user = get_by_data(title)
        if user:
            todos.remove(user)
        return {"message": "Deleted"}
        
api.add_resource(Todo, "/api/v1/todos")
api.add_resource(Todo2, "/api/v1/todos/<string:title>", methods=['PUT', 'DELETE'])
