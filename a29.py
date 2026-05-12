class DigitalWallet:

    # Class Variables
    company_name = "PayFlow"
    max_wallet_limit = 50000

    # Constructor
    def __init__(self, user_name, balance):
        self.user_name = user_name
        self.balance = balance
        self.transaction_history = []

    # Instance Method
    def add_money(self, amount):

        if not DigitalWallet.is_valid_amount(amount):
            print("Invalid amount")
            return

        if self.balance + amount > DigitalWallet.max_wallet_limit:
            print("Wallet limit exceeded")
            return

        self.balance += amount
        self.transaction_history.append(f"Added: {amount}")

        print(f"{amount} added successfully")

    # Instance Method
    def pay(self, amount):

        if not DigitalWallet.is_valid_amount(amount):
            print("Invalid amount")
            return

        if amount > self.balance:
            print("Insufficient balance")
            return

        final_amount = DigitalWallet.apply_transaction_fee(amount)

        self.balance -= final_amount
        self.transaction_history.append(f"Paid: {final_amount}")

        print(f"Payment successful after fee deduction: {final_amount}")

    # Instance Method
    def check_balance(self):
        print("Current Balance:", self.balance)

    # Instance Method
    def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    # Class Method
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name
        print("Company name changed to:", cls.company_name)

    # Static Method
    @staticmethod
    def is_valid_amount(amount):

        # Bonus validation
        if amount <= 0:
            return False

        if amount > 10000:
            return False

        return True

    # Static Method
    @staticmethod
    def apply_transaction_fee(amount):

        fee = amount * 0.02
        final_amount = amount + fee

        return final_amount


# Creating Objects
user1 = DigitalWallet("Aravind", 5000)
user2 = DigitalWallet("Akshay", 8000)

# Wallet Operations
user1.add_money(2000)
user1.check_balance()

user1.pay(1000)
user1.check_balance()

user1.show_transaction_history()

# Class Method Usage
DigitalWallet.change_company_name("FastPay")

print("Company Name:", user1.company_name)
print("Company Name:", user2.company_name)


# -------------------------------
# Thinking Questions Answers
# -------------------------------

"""
1. Why is add_money an instance method?

Because it works with individual user data such as balance.
Each wallet object has its own balance, so the method needs access to self.


2. Why is change_company_name a class method?

Because company_name is shared by all wallet users.
Class methods modify class-level data using cls.


3. Why is is_valid_amount a static method?

Because validation logic does not depend on object data or class data.
It only checks the given input amount.


4. What happens if apply_transaction_fee is implemented as an instance method?

It would unnecessarily require object creation to use fee calculation.
The logic is independent of object state, so static method is the correct choice.
"""