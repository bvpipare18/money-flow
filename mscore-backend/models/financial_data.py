from pymongo import MongoClient

client = MongoClient('mongodb://mongodb:27017/')
db = client['mscore']

class FinancialData:
    def __init__(self, member_id, income, expenses):
        self.member_id = member_id
        self.income = income
        self.expenses = expenses

    def save(self):
        financial_data = db['financial_data']
        result = financial_data.insert_one({
            'member_id': self.member_id,
            'income': self.income,
            'expenses': self.expenses
        })
        return result.inserted_id

    @staticmethod
    def get_by_member_id(member_id):
        financial_data = db['financial_data']
        return list(financial_data.find({'member_id': member_id}))
