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
        
def get_by_data(data):
    for x in todos:
         if x[title] == "title":
             return x


class Todo2(Resource):

    def get(self, title):
        try:
            data = request.json(todos[title])
            return data
        except KeyError:
            return Response("Not found", status=404)
        
#        return todos[title]
        
#        for x in todos:
#            if x["title"] == title:      
              
#        data = todos[title]
#        for el in data:
#            if el['title'] == title:
#                return el
#        return Response("Data not found", 404)

    def put(self, title, data):
        todos[title] = request.json.get('text')
        for x in range(len(todos[title])):
            if todos[title][x]['title'] == title:
                todos[title][x] = data
                break
            return todos[title]

    def delete(self, title):
        todos[title] = request.json.get('text')
        for x in range(len(todos[title])):
            if todos[title][x]['title'] == title:
                del todos[title]
                break
            return Response("", 204)


api.add_resource(Todo, "/api/v1/todos")
api.add_resource(Todo2, "/api/v1/todos/<int:title>")



#    def get(self, title):
#       user = get_by_data(title)
#        if not user:
#            return {"error": "User not found"}
#        return user

# @classmethod
# def get_by_id(cls, id):
#     data = cls.get_file_data(cls.file)
#     for el in data:
#         if el['id'] == id:
#             return el
#
#     raise Exception("Not found")

# def get(self, id):
#     return Salon.get_by_id(id)


#    def put(self, title):
#        user = get_by_data(title)
#        if user:
#            todos.remove(user)
#            todos.append(request.json)
#        return todos

# def update_by_id(cls, id, data):
#     items = cls.get_file_data(cls.file)
#     for i in range(len(items)):
#         if items[i]['id'] == id:
#             items[i] = data
#             break
#     cls.save_to_file(items)

# def put(self, id):
#     data = request.json
#     Salon.update_by_id(id, data)
#     return Salon.get_by_id(id)


# @classmethod
# def delete_by_id(cls, id):
#     items = cls.get_file_data(cls.file)
#     for i in range(len(items)):
#         if items[i]['id'] == id:
#             del items[i]
#             break
#     cls.save_to_file(items)
#
# def delete(self, id):
#     Salon.delete_by_id(id)
#     return "", 204

