# Abstract class Implementation
from abc import ABC, abstractmethod

class BankAccount(ABC):
  @abstractmethod
  def __init__(self):
    pass
  
  def account_no(self):
    return self.account_no
  
  def account_holders(self):
    return self.account_holders
  
  def add_account_holder(self, account_holder):
    self.account_holders.append(account_holder)
  
  def current_balance(self):
    return self.current_balance
  
  @abstractmethod
  def deposit(self):
    pass
  
  @abstractmethod
  def withdraw(self):
    pass
  
  @abstractmethod
  def accumulate_interest(self):
    pass
