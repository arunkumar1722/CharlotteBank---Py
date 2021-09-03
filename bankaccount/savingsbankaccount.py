# Concrete implementation of Bank Account Abstraction representing Savings Bank Account
from .bankaccount import BankAccount

class SavingsBankAccount(BankAccount):
    def __init__(self, account_no, account_holders, initial_deposit):
        if initial_deposit < 100:
          raise Exception('Minimum initial deposit should be 100')
        self.account_no = account_no
        self.account_holders = account_holders.split(',')
        self.current_balance = initial_deposit

    def deposit(self, deposit_amount):
        if deposit_amount <= 0:
          raise Exception('Deposit Amount should be > 0')
        self.current_balance += deposit_amount
    
    def withdraw(self, withdraw_amount):
        if withdraw_amount + 100 > self.current_balance:
          raise Exception('Minimum Balance should be 100')
        self.current_balance -= withdraw_amount
    
    def accumulate_interest(self):
        # Savings Bank Account interest based on current balance
        if self.current_balance < 2000:
          interest_rate = 0.01
        elif self.current_balance >= 2000 and self.current_balance < 12000:
          interest_rate = 0.05
        elif self.current_balance >= 12000:
          interest_rate = 0.1
        interest = self.current_balance * interest_rate / 100
        self.current_balance += interest
