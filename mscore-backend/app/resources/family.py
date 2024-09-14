from flask_restful import Resource
from flask import Response, request
import json

class FamilyResource(Resource):
    def get(self):
        data = {
            "message": "Welcome to the M-Score system backend!",
            "note": "This is where you will manage family member data."
        }
        return Response(
            json.dumps(data),
            mimetype='application/json',
            status=200
        )

    def post(self):
        data = request.get_json()
        # Process and save the data to the database (placeholder logic)
        response_data = {
            "message": "Family member created",
            "data": data
        }
        return Response(
            json.dumps(response_data),
            mimetype='application/json',
            status=201
        )

    def put(self):
        data = request.get_json()
        # Replace existing data with new data (placeholder logic)
        response_data = {
            "message": "Family member updated",
            "data": data
        }
        return Response(
            json.dumps(response_data),
            mimetype='application/json',
            status=200
        )

    def patch(self):
        data = request.get_json()
        # Partially update the resource (placeholder logic)
        response_data = {
            "message": "Family member partially updated",
            "data": data
        }
        return Response(
            json.dumps(response_data),
            mimetype='application/json',
            status=200
        )

    def delete(self):
        # Extract identifier from request (placeholder logic)
        response_data = {
            "message": "Family member deleted"
        }
        return Response(
            json.dumps(response_data),
            mimetype='application/json',
            status=200
        )
