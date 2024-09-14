from flask import Flask
from flask_restful import Api
from resources.family_resource import FamilyResource
from resources.financial_resource import FinancialResource

app = Flask(__name__)
api = Api(app)

# Add resources to API
api.add_resource(FamilyResource, '/family', '/family/<string:member_id>')
api.add_resource(FinancialResource, '/financial', '/financial/<string:member_id>')

if __name__ == '__main__':
    app.run(debug=True)
