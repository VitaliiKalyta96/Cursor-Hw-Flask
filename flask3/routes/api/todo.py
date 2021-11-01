from app import app, api
from flask import request, Response
from flask_restful import Resource


todos = []

class Todo(Resource):
    def get(self):
        return todos

    def post(self):
        todos.append(request.json)
        return todos
        
        
# def get_by_data(data):
#    for x in todos:
#        if x.get("title") == int(data):
#            return x


class Todo2(Resource):

#    def get(self, title):
#       user = get_by_data(title)
#        if not user:
#            return {"error": "User not found"}
#        return user

    def get(self, title):
        data = todos[title]
        if not data in todos:
            return Response("Data not found", 404)
        return todos[title]
        
#    def put(self, title):
#        user = get_by_data(title)
#        if user:
#            todos.remove(user)
#            todos.append(request.json)
#        return todos  

    def put(self, title):  
        todos[title] =  request.json.get('text')
        return todos[title]

    def delete(self, title):
        del todos[title]
        return Response("", 204)
        
api.add_resource(Todo, "/api/v1/todos")
api.add_resource(Todo2, "/api/v1/todos/<int:title>", methods=['PUT', 'DELETE'])

