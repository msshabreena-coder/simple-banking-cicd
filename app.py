
class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = float(balance)

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.balance += amount
        return self.balance


def main():
    account = BankAccount()

    while True:
        print("\n===== SIMPLE BANKING APPLICATION =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print(f"Current Balance: Rs. {account.check_balance():.2f}")

        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: Rs. "))
                balance = account.deposit(amount)
                print(f"Deposit successful. Balance: Rs. {balance:.2f}")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "3":
            print("Thank you for using the banking application.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
