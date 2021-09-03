# Main class to demonstrate Bank Account
from bankaccount.checkingbankaccount import CheckingBankAccount
from bankaccount.savingsbankaccount import SavingsBankAccount
import random

class Main:
  # Checking Account
  checking_account = CheckingBankAccount(str(random.randrange(0,10**10)), 'Alejandro Lopez-Perez')
  print('Account No:', checking_account.account_no)

  checking_account.deposit(1500)
  print(checking_account.current_balance)

  checking_account.withdraw(150)
  print(checking_account.current_balance)

  checking_account.accumulate_interest()
  print(checking_account.current_balance)

  checking_account.withdraw(750)
  print(checking_account.current_balance)

  checking_account.accumulate_interest()
  print(checking_account.current_balance)

  # Savings Account
  savings_account = SavingsBankAccount(str(random.randrange(0,10**10)), 'Sasha Ivanov', 600)
  print('Account No:', savings_account.account_no)

  savings_account.accumulate_interest()
  print(savings_account.current_balance)

  savings_account.deposit(150)
  print(savings_account.current_balance)

  savings_account.accumulate_interest()
  print(savings_account.current_balance)

  savings_account.withdraw(600)
  print(savings_account.current_balance)