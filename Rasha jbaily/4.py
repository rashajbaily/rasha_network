class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount

    def print_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")
        print(f"Interest Rate: {self.interest_rate}")

    # Create an instance of BankAccount


bank_account = BankAccount("123456789", "Alice")
bank_account.deposit(1000)
print("Balance after deposit: $", bank_account.get_balance())
bank_account.withdraw(500)
print("Balance after withdrawal: $", bank_account.get_balance())

# Create an instance of SavingsAccount
savings_account = SavingsAccount("987654321", "Bob", 0.05)
savings_account.deposit(2000)
savings_account.apply_interest()
savings_account.print_info()
