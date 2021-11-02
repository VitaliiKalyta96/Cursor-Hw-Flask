from app import app, api
from flask import request, Response
from flask_restful import Resource
from models import Salon


class SalonResource(Resource):

    def get(self):
        salon = Salon.get_all()
        limit = int(request.args.get('limit', False))
        if limit:
            return salon[:limit]
        return salon

    def post(self):
        request_data = request.json
        salon = Salon(
            request_data['id'],
            request_data['name'],
            request_data['director_id'],
            request_data['city'],
            request_data['address'],
        )
        salon.save()
        return salon._generate_dict()


class SalonSingleResource(Resource):

    def get(self, id):
        return Salon.get_by_id(id)

    def put(self, id):
        data = request.json
        Salon.update_by_id(id, data)
        return Salon.get_by_id(id)

    def delete(self, id):
        Salon.delete_by_id(id)
        return "", 204
        

class SalonDirectorResource(Resource):
    def get(self, id):
        try:
            salon = Salon.get_by_id(id)
            director = Salon.director(salon['director_id'])
            if director is None:
                return "Director Not Found", 404
            return director
        except Exception:
            return "Not Found", 404
api.add_resource(PlantResource, "/api/v1/salons")            
api.add_resource(PlantDirectorResource, '/api/v1/salons/<int:id>/director')
api.add_resource(PlantSingleResource, "/api/v1/salons/<int:id>")  
