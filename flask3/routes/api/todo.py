from app import app, api
from flask import request, Response
from flask_restful import Resource, abort


todos = {}


class Todo(Resource):

    def get(self):
        return todos

    def post(self):
        todos[request.json.get('title_id', 'text')] = request.json.get('int', 'text')
        return todos


class TodoEdit(Resource):

    def get(self, title_id):
        try:
            data = {title_id: todos[title_id]}
        except KeyError:
            return abort(404, message="This title_id {} not found.".format(title_id))
        return data

    def put(self, title_id):
        try:
            todos[title_id] = request.json.get('text')
            return {title_id: todos[title_id]}
        except KeyError:
            return abort(404, message="This title_id {} not found.".format(title_id))
            
    def delete(self, title_id):
        try:
            del todos[title_id]
            return Response(todos, status=204)
        except KeyError:
            return abort(404, message="This title_id {} not found.".format(title_id))


api.add_resource(Todo, '/api/v1/todos')
api.add_resource(TodoEdit, '/api/v1/todos/<int:title_id>')
