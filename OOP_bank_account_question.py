class BankAccount:
    def __init__(self, account_id):
        self.account_id = account_id
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id):
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = BankAccount(account_id)
        return True
    
    def deposit(self, account_id, amount):
        if account_id not in self.accounts:
            return False
        self.accounts[account_id].deposit(amount)
        return True
    
    def withdraw(self, account_id, amount):
        if account_id not in self.accounts:
            return False
        return self.accounts[account_id].withdraw(amount)
    
    def transfer(self, from_account, to_account, amount):
        if from_account not in self.accounts or to_account not in self.accounts:
            return False
        if not self.accounts[from_account].withdraw(amount):
            return False
        self.accounts[to_account].deposit(amount)
        return True
    

bank = BankSystem()

bank.create_account(1234)
bank.create_account(5678)

bank.deposit(1234, 100)
bank.withdraw(1234, 50)

print(bank.accounts[1234].balance) # 50

bank.transfer(1234, 5678, 20)

print(bank.accounts[1234].balance) # 30
print(bank.accounts[5678].balance) # 20

print(bank.transfer(5678, 1234, 100)) # False


