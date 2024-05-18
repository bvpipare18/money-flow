import random
import string

class FamilyMember:
    def __init__(self, name, income, spending_accounts, invest_accounts):
        self.id = self.generate_id(name)
        self.name = name
        self.income = income
        self.spending_accounts = spending_accounts
        self.invest_accounts = invest_accounts

    def generate_id(self, name):
        random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        return name[:3].upper() + random_suffix

    def record_transaction(self, transaction_type, amount):
        if transaction_type == "spend":
            if "total" not in self.spending_accounts:
                self.spending_accounts["total"] = 0
            self.spending_accounts["total"] += amount
            self.income -= amount
        elif transaction_type == "invest":
            if "total" not in self.invest_accounts:
                self.invest_accounts["total"] = 0
            self.invest_accounts["total"] += amount
            self.income -= amount
        else:
            print("Invalid transaction type. Please choose 'spend' or 'invest'.")

    def display_accounts(self):
        print(f"\nAccounts for {self.name}:")
        print(f"Income: Rupees {self.income}")
        print("Spending Accounts:")
        for acc_name, balance in self.spending_accounts.items():
            print(f"{acc_name}: Rupees {balance}")
        print("Invest Accounts:")
        for acc_name, balance in self.invest_accounts.items():
            print(f"{acc_name}: Rupees {balance}")
