from family_member import FamilyMember
from config_loader import load_config
from transaction_manager import record_transaction
from display_manager import display_family_members, display_totals

def calculate_totals(family_members):
    total_income = sum(member.income for member in family_members)
    total_spend = sum(member.spending_accounts.get("total", 0) for member in family_members)
    total_invest = sum(member.invest_accounts.get("total", 0) for member in family_members)
    return total_income, total_spend, total_invest

def select_family_name():
    return input("Enter family name: ")

def main():
    # Load settings from the INI file
    config = load_config('config.ini')

    # Define family members
    family_members = []
    for member, income in config['FamilyMembers'].items():
        family_members.append(FamilyMember(member, float(income), {"total": 0}, {"total": 0}))

    # Ask for family name
    family_name = select_family_name()

    # Recording transactions
    while True:
        display_family_members(family_members)
        member_choice = input("Enter the ID of the family member or type 'exit' to exit: ")

        # Check if the user wants to exit
        if member_choice.lower() == "exit":
            break

        # Validate user input
        try:
            member_idx = int(member_choice) - 1
            if 0 <= member_idx < len(family_members):
                selected_member = family_members[member_idx]
            else:
                print("Invalid family member ID. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid family member ID.")
            continue

        transaction_type = input("Enter transaction type ('spend' or 'invest'), or type 'exit' to exit: ")

        # Check if the user wants to exit the current transaction
        if transaction_type.lower() == "exit":
            continue

        # Check if the transaction type is valid
        if transaction_type.lower() not in ["spend", "invest"]:
            print("Invalid transaction type. Please choose 'spend' or 'invest'.")
            continue

        # Check if the user wants to exit the current transaction
        amount = input("Enter transaction amount: Rupees, or type 'exit' to exit: ")
        if amount.lower() == "exit":
            continue

        # Validate and record the transaction
        try:
            amount = float(amount)
            record_transaction(selected_member, transaction_type.lower(), amount)
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            continue

        choice = input("Do you want to record another transaction? (yes/no): ")
        if choice.lower() != "yes":
            break

    # Calculate existing totals
    existing_income, existing_spend, existing_invest = calculate_totals(family_members)

    # Calculate updated totals
    total_income, total_spend, total_invest = calculate_totals(family_members)
    
    # Display totals with family name and details
    display_totals(existing_income, existing_spend, existing_invest, total_income, total_spend, total_invest, family_members, family_name)


if __name__ == "__main__":
    main()
