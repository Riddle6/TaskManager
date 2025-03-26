'''
Create different accounts, and transactions from each
'''
# Define the function to collect data
def create_bank():
# Define the primary dictionary
    bank = {}
    # Collect data for bank
    while True:
        account = input("Enter the name of the account (type 'done' to exit): ").strip()

        if account.lower() == 'done':
            break

        if account not in bank:
            bank[account] = {} # Create a key in the bank dictionary called account, set to an empty dictionary

        while True:
            
            trans_type = input("Enter a type of transaction: (or type 'done' to exit): ").strip()

            if trans_type.lower() == 'done':
                break

            trans_amount = float(input("Enter the amount: "))

            # bank[account][trans_type] = trans_type
            bank[account][trans_amount] = trans_amount

    print(f"\n{bank}") # Testing what's been entered.
    return bank

def display_bank(bank):
    print(f"\nBank Accounts & Transactions:\n")

    for accounts, trans_amount in bank.items():
        print(f"Account: {accounts}")
            # Key
        for transaction, amount in trans_amount.items():
            print(f" - Amount: ${amount:.2f}")

bank_account = create_bank()

display_bank(bank_account)