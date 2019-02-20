class BankAccount:
    """ Performs functions of a bank account """

    interest_rate = 3.0
    accounts = []

    @classmethod
    def create(cls):
        new_account = BankAccount()
        cls.accounts.append(new_account)
        return new_account

    @classmethod
    def total_funds(cls):
        total = 0
        for account in cls.accounts:
            total += account.balance
        return total

    @classmethod
    def interest_time(cls):
        for account in cls.accounts:
            account.balance = account.balance + (account.balance * (cls.interest_rate/100))


    def __init__(self):
        self.balance = 0

    def __str__(self):
        return "Account Balance: ${:.2f}".format(self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Error: Insufficient Funds!")


#-----------------------------------------------------------------------------
# Testing create method
my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account)
print(your_account)
#-----------------------------------------------------------------------------
# Testing withdraw and deposit methods
my_account.deposit(1000)
your_account.deposit(500)
# your_account.withdraw(550)
my_account.withdraw(750)
print(my_account)
print(your_account)
#-----------------------------------------------------------------------------
print("Total Bank Funds: ${:.2f}".format(BankAccount.total_funds()))
#-----------------------------------------------------------------------------
BankAccount.interest_time()
print("Account Balance: ${:.2f}".format(my_account.balance))
print("Account Balance: ${:.2f}".format(your_account.balance))
