def display_family_members(members):
    print("Available family members:")
    for idx, member in enumerate(members, start=1):
        print(f"{idx}. {member.name} (ID: {member.id})")
    print("Exit")

def display_totals(existing_income, existing_spend, existing_invest, total_income, total_spend, total_invest, family_members, family_name):
    print(f"\nHi {family_name} Family,\n")
    print("Existing Details:")
    print("Existing Income amount:", existing_income)
    print("Existing Spend amount:", existing_spend)
    print("Existing Invest-It amount:", existing_invest)
    for member in family_members:
        member.display_accounts()
    print("\nUpdated Details:")
    print("Current Income amount:", total_income)
    print("Current Spend amount:", total_spend)
    print("Current Invest-It amount:", total_invest)
