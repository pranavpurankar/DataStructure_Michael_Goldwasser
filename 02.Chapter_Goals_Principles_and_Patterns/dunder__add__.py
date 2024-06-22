class Cisco:

    def __init__(self, initial_deposit):
        self.balance = initial_deposit

    def print_balance(self):
        print("Balance: ", self.balance)

    def __add__(self, other):
        total = self.balance + other.balance
        return BankAccount(total)


account1 = BankAccount(1000)
account2 = BankAccount(2000)

new_account = account1 + account1
new_account.print_balance()
