# Concrete implementation of Bank Account Abstraction representing Checking Bank Account
from .bankaccount import BankAccount

class CheckingBankAccount(BankAccount):
    def __init__(self, account_no, account_holders, initial_deposit = 0):
        self.account_no = account_no
        self.account_holders = account_holders.split(',')
        self.current_balance = initial_deposit

    def deposit(self, deposit_amount):
        if deposit_amount <= 0:
          raise Exception('Deposit Amount should be > 0')
        self.current_balance += deposit_amount
    
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.current_balance:
          raise Exception('Insufficient Balance')
        self.current_balance -= withdraw_amount
    
    def accumulate_interest(self):
        # Checking bank account flat interest
        interest = self.current_balance * 0.01 / 100
        self.current_balance += interest
