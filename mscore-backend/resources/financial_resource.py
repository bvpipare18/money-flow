from flask_restful import Resource
from flask import request, Response
import json
from models.financial_data import FinancialData

class FinancialResource(Resource):
    def get(self, member_id):
        data = FinancialData.get_by_member_id(member_id)
        return Response(
            json.dumps(data, default=str),
            mimetype='application/json',
            status=200
        )

    def post(self):
        data = request.get_json()
        financial = FinancialData(member_id=data['member_id'], income=data['income'], expenses=data['expenses'])
        financial_id = financial.save()
        return Response(
            json.dumps({"message": "Financial data created", "id": str(financial_id)}),
            mimetype='application/json',
            status=201
        )
