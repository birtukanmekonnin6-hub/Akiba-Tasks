
transactions = []


def deposit(balance, amount):
    if amount <= 0:
        print("Invalid deposit amount!")
    else:
        balance += amount
        transactions.append({
            "type": "Deposit",
            "amount": amount,
            "balance": balance
        })
        print("Deposit successful!")

    return balance


def withdrawal(balance, amount):
    if amount <= 0:
        print("Invalid withdrawal amount!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        transactions.append({
            "type": "Withdrawal",
            "amount": amount,
            "balance": balance
        })
        print("Withdrawal successful!")

    return balance


def current_balance(balance):
    print(f"Current balance: {balance} Birr")


def record_transaction():
    print("\nTransaction History")

    if not transactions:
        print("No transactions recorded.")
    else:
        for transaction in transactions:
            print(
                f"{transaction['type']}: "
                f"{transaction['amount']} Birr | "
                f"Balance: {transaction['balance']} Birr"
            )


def generate_transaction_summary(balance):
    total_deposits = 0
    total_withdrawals = 0

    for transaction in transactions:
        if transaction["type"] == "Deposit":
            total_deposits += transaction["amount"]
        else:
            total_withdrawals += transaction["amount"]

    print("\nTransaction Summary")
    print("-------------------")
    print(f"Total deposits: {total_deposits} Birr")
    print(f"Total withdrawals: {total_withdrawals} Birr")
    print(f"Number of transactions: {len(transactions)}")
    print(f"Current balance: {balance} Birr")

balance=2000

while True:
    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check current balance")
    print("4. Record transaction history")
    print("5. Generate transaction summary")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        balance = deposit(balance, amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        balance = withdrawal(balance, amount)

    elif choice == "3":
        current_balance(balance)

    elif choice == "4":
        record_transaction()

    elif choice =="5":
        print("Option 5 selected!")
        generate_transaction_summary(balance)
    elif choice == "6":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice. Please try again.")

