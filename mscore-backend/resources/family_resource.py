from flask_restful import Resource
from flask import request, Response
import json
from bson.objectid import ObjectId
from models.family_member import FamilyMember

class FamilyResource(Resource):
    
    def get(self, member_id=None):
        if member_id:
            # Validate ObjectId
            if not ObjectId.is_valid(member_id):
                return Response(
                    json.dumps({"error": "Invalid ID format"}),
                    mimetype='application/json',
                    status=400
                )
            
            member = FamilyMember.get_by_id(member_id)
            if member:
                return Response(
                    json.dumps(member, default=str),
                    mimetype='application/json',
                    status=200
                )
            return Response(
                json.dumps({"error": "Family member not found"}),
                mimetype='application/json',
                status=404
            )
        
        # Get all family members
        members = FamilyMember.get_all()
        return Response(
            json.dumps(members, default=str),
            mimetype='application/json',
            status=200
        )

    def post(self):
        data = request.get_json()
        if not data or 'name' not in data or 'age' not in data:
            return Response(
                json.dumps({"error": "Invalid input"}),
                mimetype='application/json',
                status=400
            )
        
        member = FamilyMember(name=data['name'], age=data['age'], job=data.get('job'))
        member_id = member.save()
        return Response(
            json.dumps({"message": "Family member created", "id": str(member_id)}),
            mimetype='application/json',
            status=201
        )

    def put(self, member_id):
        # Validate ObjectId
        if not ObjectId.is_valid(member_id):
            return Response(
                json.dumps({"error": "Invalid ID format"}),
                mimetype='application/json',
                status=400
            )
        
        data = request.get_json()
        if not data:
            return Response(
                json.dumps({"error": "Invalid input"}),
                mimetype='application/json',
                status=400
            )
        
        updated = FamilyMember.update(member_id, data)

        if updated:
            return Response(
                json.dumps({"message": "Family member updated"}),
                mimetype='application/json',
                status=200
            )
        return Response(
            json.dumps({"error": "Family member not found"}),
            mimetype='application/json',
            status=404
        )

    def delete(self, member_id):
        # Validate ObjectId
        if not ObjectId.is_valid(member_id):
            return Response(
                json.dumps({"error": "Invalid ID format"}),
                mimetype='application/json',
                status=400
            )
        
        deleted = FamilyMember.delete(member_id)
        if deleted:
            return Response(
                json.dumps({"message": "Family member deleted"}),
                mimetype='application/json',
                status=200
            )
        return Response(
            json.dumps({"error": "Family member not found"}),
            mimetype='application/json',
            status=404
        )
