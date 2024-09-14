from pymongo import MongoClient
from bson.objectid import ObjectId

# MongoDB client setup
client = MongoClient("mongodb://mongodb:27017/mscore_database")
db = client['mscore_database']
collection = db['family_members']

class FamilyMember:
    def __init__(self, name, age, job=None):
        self.name = name
        self.age = age
        self.job = job

    def save(self):
        result = collection.insert_one({
            'name': self.name,
            'age': self.age,
            'job': self.job
        })
        return result.inserted_id

    @staticmethod
    def get_by_id(member_id):
        try:
            return collection.find_one({'_id': ObjectId(member_id)})
        except Exception as e:
            return None

    @staticmethod
    def get_all():
        return list(collection.find())

    @staticmethod
    def update(member_id, data):
        result = collection.update_one(
            {'_id': ObjectId(member_id)},
            {'$set': data}
        )
        return result.modified_count > 0

    @staticmethod
    def delete(member_id):
        result = collection.delete_one({'_id': ObjectId(member_id)})
        return result.deleted_count > 0
