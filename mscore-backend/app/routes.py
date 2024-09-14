from app.resources.family import FamilyResource

def init_routes(api):
    # Define routes here
    api.add_resource(FamilyResource, '/family')
