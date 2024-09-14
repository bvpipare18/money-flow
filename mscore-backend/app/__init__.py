from flask import Flask
from flask_restful import Api

def create_app():
    app = Flask(__name__)
    
    # Initialize Flask-RESTful API
    api = Api(app)
    
    # Import the routes
    from .routes import init_routes
    init_routes(api)
    
    return app
